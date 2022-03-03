"""empty message

Revision ID: 959f3465bf95
Revises: 
Create Date: 2022-03-03 13:18:21.886162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '959f3465bf95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=10), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('distance', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    # ### end Alembic commands ###
