"""Init migration

Revision ID: 08219a3df140
Revises: 
Create Date: 2020-12-09 18:56:34.955498

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '08219a3df140'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mid', sa.Integer(), nullable=True),
    sa.Column('mname', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mid')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vid', sa.Integer(), nullable=True),
    sa.Column('vname', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('vid')
    )
    op.drop_table('alembic_version-old')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alembic_version-old',
    sa.Column('version_num', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=32), nullable=False),
    sa.PrimaryKeyConstraint('version_num'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('vehicle')
    op.drop_table('mission')
    # ### end Alembic commands ###
