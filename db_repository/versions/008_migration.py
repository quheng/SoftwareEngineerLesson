from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
order_manager = Table('order_manager', post_meta,
    Column('orderID', String(length=20), primary_key=True, nullable=False),
    Column('orderName', String(length=50)),
    Column('buyer', String(length=20)),
    Column('seller', String(length=20)),
    Column('orderItems', String(length=200)),
    Column('orderStatus', Integer),
    Column('orderTime', Time),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order_manager'].columns['buyer'].create()
    post_meta.tables['order_manager'].columns['orderItems'].create()
    post_meta.tables['order_manager'].columns['seller'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order_manager'].columns['buyer'].drop()
    post_meta.tables['order_manager'].columns['orderItems'].drop()
    post_meta.tables['order_manager'].columns['seller'].drop()
