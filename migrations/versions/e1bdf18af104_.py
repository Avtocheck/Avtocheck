"""empty message

Revision ID: e1bdf18af104
Revises: 05f9ea70c74e
Create Date: 2021-01-31 19:46:03.981309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1bdf18af104'
down_revision = '05f9ea70c74e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 'role', ['name'], unique=True)
    # ### end Alembic commands ###
