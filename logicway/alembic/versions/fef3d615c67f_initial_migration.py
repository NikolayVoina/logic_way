"""Initial migration

Revision ID: fef3d615c67f
Revises: 
Create Date: 2024-09-14 12:40:34.966074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fef3d615c67f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency',
    sa.Column('agency_id', sa.String(), nullable=False),
    sa.Column('agency_name', sa.String(), nullable=True),
    sa.Column('agency_url', sa.String(), nullable=True),
    sa.Column('agency_timezone', sa.String(), nullable=True),
    sa.Column('agency_phone', sa.String(), nullable=True),
    sa.Column('agency_lang', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('agency_id')
    )
    op.create_table('calendar',
    sa.Column('service_id', sa.String(), nullable=False),
    sa.Column('monday', sa.Boolean(), nullable=True),
    sa.Column('tuesday', sa.Boolean(), nullable=True),
    sa.Column('wednesday', sa.Boolean(), nullable=True),
    sa.Column('thursday', sa.Boolean(), nullable=True),
    sa.Column('friday', sa.Boolean(), nullable=True),
    sa.Column('saturday', sa.Boolean(), nullable=True),
    sa.Column('sunday', sa.Boolean(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('service_id')
    )
    op.create_table('routes',
    sa.Column('route_id', sa.String(), nullable=False),
    sa.Column('agency_id', sa.String(), nullable=True),
    sa.Column('route_short_name', sa.String(), nullable=True),
    sa.Column('route_long_name', sa.String(), nullable=True),
    sa.Column('route_type', sa.Integer(), nullable=True),
    sa.Column('route_color', sa.String(), nullable=True),
    sa.Column('route_text_color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('route_id')
    )
    op.create_table('shapes',
    sa.Column('shape_id', sa.String(), nullable=False),
    sa.Column('shape_pt_lat', sa.Float(), nullable=True),
    sa.Column('shape_pt_lon', sa.Float(), nullable=True),
    sa.Column('shape_pt_sequence', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('shape_id')
    )
    op.create_table('stop_times',
    sa.Column('trip_id', sa.String(), nullable=False),
    sa.Column('arrival_time', sa.Time(), nullable=True),
    sa.Column('departure_time', sa.Time(), nullable=True),
    sa.Column('stop_id', sa.String(), nullable=True),
    sa.Column('stop_sequence', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('trip_id', 'stop_sequence')
    )
    op.create_table('stops',
    sa.Column('stop_id', sa.String(), nullable=False),
    sa.Column('stop_name', sa.String(), nullable=True),
    sa.Column('stop_lat', sa.Float(), nullable=True),
    sa.Column('stop_lon', sa.Float(), nullable=True),
    sa.Column('zone_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('stop_id')
    )
    op.create_table('trips',
    sa.Column('route_id', sa.String(), nullable=True),
    sa.Column('service_id', sa.String(), nullable=True),
    sa.Column('trip_id', sa.String(), nullable=False),
    sa.Column('trip_headsign', sa.String(), nullable=True),
    sa.Column('direction_id', sa.Integer(), nullable=True),
    sa.Column('block_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('trip_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trips')
    op.drop_table('stops')
    op.drop_table('stop_times')
    op.drop_table('shapes')
    op.drop_table('routes')
    op.drop_table('calendar')
    op.drop_table('agency')
    # ### end Alembic commands ###