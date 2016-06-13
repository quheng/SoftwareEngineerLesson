from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
order_manager = Table('order_manager', post_meta,
    Column('orderID', Integer, primary_key=True, nullable=False),
    Column('buyer', Integer),
    Column('seller', Integer),
    Column('orderAmount', Float),
    Column('orderItems', String(length=200)),
    Column('orderStatus', Integer),
    Column('orderTime', DateTime),
    Column('captcha', String(length=10)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order_manager'].columns['captcha'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order_manager'].columns['captcha'].drop()
