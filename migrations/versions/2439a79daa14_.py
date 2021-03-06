"""empty message

Revision ID: 2439a79daa14
Revises: 
Create Date: 2016-12-05 07:50:12.282000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2439a79daa14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue_owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=20), nullable=True),
    sa.Column('province_state', sa.String(length=20), nullable=True),
    sa.Column('postal_zip_code', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_venue_owners_name'), 'venue_owners', ['name'], unique=True)
    op.create_table('venues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('website', sa.String(length=200), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('slug', sa.String(length=50), nullable=True),
    sa.Column('street_number', sa.Integer(), nullable=True),
    sa.Column('route_short', sa.String(length=150), nullable=True),
    sa.Column('route_long', sa.String(length=150), nullable=True),
    sa.Column('city_short', sa.String(length=50), nullable=True),
    sa.Column('city_long', sa.String(length=50), nullable=True),
    sa.Column('admin_area_level_2_long', sa.String(length=50), nullable=True),
    sa.Column('admin_area_level_2_short', sa.String(length=50), nullable=True),
    sa.Column('admin_area_level_1_long', sa.String(length=50), nullable=True),
    sa.Column('admin_area_level_1_short', sa.String(length=50), nullable=True),
    sa.Column('country_long', sa.String(length=50), nullable=True),
    sa.Column('country_short', sa.String(length=50), nullable=True),
    sa.Column('postal_code', sa.String(length=10), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lng', sa.Float(), nullable=True),
    sa.Column('formatted_address', sa.String(length=150), nullable=True),
    sa.Column('import_id', sa.Integer(), nullable=True),
    sa.Column('import_address', sa.String(length=150), nullable=True),
    sa.Column('import_raw_address', sa.String(length=200), nullable=True),
    sa.Column('notes', sa.String(length=150), nullable=True),
    sa.Column('venue_owner_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['venue_owner_id'], ['venue_owners.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('import_id'),
    sa.UniqueConstraint('postal_code')
    )
    op.create_index(op.f('ix_venues_name'), 'venues', ['name'], unique=False)
    op.create_table('ice_pads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ice_pads_name'), 'ice_pads', ['name'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ice_pads_name'), table_name='ice_pads')
    op.drop_table('ice_pads')
    op.drop_index(op.f('ix_venues_name'), table_name='venues')
    op.drop_table('venues')
    op.drop_index(op.f('ix_venue_owners_name'), table_name='venue_owners')
    op.drop_table('venue_owners')
    ### end Alembic commands ###
