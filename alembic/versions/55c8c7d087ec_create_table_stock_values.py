"""create table stock_prices

Revision ID: 55c8c7d087ec
Revises: 9fafe320f35a
Create Date: 2021-01-07 14:48:41.278266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55c8c7d087ec'
down_revision = '9fafe320f35a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stock_prices',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('stock_id', sa.Integer, sa.ForeignKey('stocks.id'), ),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('price', sa.DECIMAL(18, 2), nullable=False)
    )


def downgrade():
    op.drop_table('stock_prices')
