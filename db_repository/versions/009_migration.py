from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
order_manager = Table('order_manager', pre_meta,
    Column('orderID', VARCHAR(length=20), primary_key=True, nullable=False),
    Column('orderName', VARCHAR(length=50)),
    Column('orderStatus', INTEGER),
    Column('orderTime', TIME),
    Column('buyer', VARCHAR(length=20)),
    Column('orderItems', VARCHAR(length=200)),
    Column('seller', VARCHAR(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['order_manager'].columns['buyer'].drop()
    pre_meta.tables['order_manager'].columns['orderItems'].drop()
    pre_meta.tables['order_manager'].columns['seller'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['order_manager'].columns['buyer'].create()
    pre_meta.tables['order_manager'].columns['orderItems'].create()
    pre_meta.tables['order_manager'].columns['seller'].create()
