"""empty message

Revision ID: 7192518e04b8
Revises: 
Create Date: 2020-12-01 23:29:53.138569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7192518e04b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('farmer',
    sa.Column('transaction_ID', sa.String(), nullable=False),
    sa.Column('farmer_ID', sa.String(), nullable=True),
    sa.Column('details', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('transaction_ID')
    )
    op.create_table('product',
    sa.Column('product_id', sa.String(), nullable=False),
    sa.Column('chain_index', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('refiner',
    sa.Column('transaction_ID', sa.String(), nullable=False),
    sa.Column('refiner_ID', sa.String(), nullable=True),
    sa.Column('details', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('transaction_ID')
    )
    op.create_table('wholesaler',
    sa.Column('transaction_ID', sa.String(), nullable=False),
    sa.Column('Wholesaler_ID', sa.String(), nullable=True),
    sa.Column('details', sa.String(), nullable=True),
    sa.Column('product_Number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('transaction_ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wholesaler')
    op.drop_table('refiner')
    op.drop_table('product')
    op.drop_table('farmer')
    # ### end Alembic commands ###