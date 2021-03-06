"""Add Table uwb

Revision ID: 4359f5b04eea
Revises: 5a9c6f45c71a
Create Date: 2020-12-29 17:38:39.075959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4359f5b04eea'
down_revision = '5a9c6f45c71a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uwbmodule',
    sa.Column('uwbid', sa.Integer(), nullable=False),
    sa.Column('address', sa.Binary(), nullable=True),
    sa.Column('serial', sa.Binary(), nullable=True),
    sa.PrimaryKeyConstraint('uwbid')
    )
    op.add_column('anchorwaypoint', sa.Column('uwbid', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('anchorwaypoint', 'uwbid')
    op.drop_table('uwbmodule')
    # ### end Alembic commands ###
