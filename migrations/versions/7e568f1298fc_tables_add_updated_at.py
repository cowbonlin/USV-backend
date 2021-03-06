"""Tables add updated_at

Revision ID: 7e568f1298fc
Revises: 8f536264eca3
Create Date: 2021-02-11 01:23:55.054583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e568f1298fc'
down_revision = '8f536264eca3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('anchor_waypoint', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('commtype', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('r_anchors', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('r_uwb_veh', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('r_veh_mis', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('r_vehstate_encounter', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('uwb_module', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('vehicle', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicle', 'updated_at')
    op.drop_column('uwb_module', 'updated_at')
    op.drop_column('r_vehstate_encounter', 'updated_at')
    op.drop_column('r_veh_mis', 'updated_at')
    op.drop_column('r_uwb_veh', 'updated_at')
    op.drop_column('r_anchors', 'updated_at')
    op.drop_column('commtype', 'updated_at')
    op.drop_column('anchor_waypoint', 'updated_at')
    # ### end Alembic commands ###
