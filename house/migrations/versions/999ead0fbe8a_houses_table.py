"""houses table

Revision ID: 999ead0fbe8a
Revises: 
Create Date: 2021-12-20 08:48:47.791856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '999ead0fbe8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('house',
    sa.Column('house_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('family_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('house_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('house')
    # ### end Alembic commands ###
