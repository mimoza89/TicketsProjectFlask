"""add purchased tickets to user model

Revision ID: aa3627a07c03
Revises: 61af7189a139
Create Date: 2023-04-26 00:07:52.703326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa3627a07c03'
down_revision = '61af7189a139'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('purchased_tickets', sa.Integer(), nullable=True))
        batch_op.drop_column('card_number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('card_number', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('purchased_tickets')

    # ### end Alembic commands ###