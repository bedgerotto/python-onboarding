import sqlalchemy as sa
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import requests


def prepare_db():
    engine = sa.create_engine("mysql://bruno:password@db/stocks")
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    Stock = Base.classes.stocks
    StockPrice = Base.classes.stock_prices

    return [Session(engine), Stock, StockPrice]

def fetch_api_data():
    response = requests.get(
        'https://cloud.iexapis.com/stable/stock/FB/batch?'
        'types=chart&'
        'range=1m&'
        'last=30&'
        'token=pk_bc796a0e15a34d559a6fa9b9c9782de1&'
        'filter=close,volume,date,label,change,changePercent'
    )

    return response.json()


def main():
    print('Preparing database connection')
    session, Stock, StockPrice = prepare_db()

    print('Searching for current Stock')
    if session.query(Stock).filter_by(name='Facebook').first() is None:
        print('Not found. Creating...')
        session.add(Stock(name='Facebook'))
    else:
        print('Found stock: Facebook')
    
    current_stock = session.query(Stock).filter_by(name='Facebook').first()
    print('Fetch api data and create registers')
    data = fetch_api_data()
    for item in data['chart']:
        print("{stock_name} was ${stock_price} at {quote_date}".format(stock_name=current_stock.name, stock_price=item['close'], quote_date=item['date']))
        stock_price = session.query(StockPrice).filter_by(stock_id=current_stock.id, date=item['date']).first()
        if stock_price:
            print("Updating stock price")
            session.query(StockPrice).filter_by(id=stock_price.id).update({"price": item['close']})
        else:
            print("Creating stock price")
            session.add(StockPrice(stock_id=current_stock.id, price=item['close'], date=item['date']))
    session.commit()

main()