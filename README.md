# Python onboarding

This script fetch Facebook stocks price from a [Iexapis](https://cloud.iexapis.com) using *requests* library and stores each price in a MySQL table with SqlAlchemy



# Setting up

docker-compose build

docker-compose run --rm app alembic upgrade head

# Running

docker-compose run --rm app .venv/bin/python fetch_stocks.py
