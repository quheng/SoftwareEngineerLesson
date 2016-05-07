from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
buyer = Table('buyer', post_meta,
    Column('buyerID', String(length=20), primary_key=True, nullable=False),
    Column('buyerName', String(length=50)),
    Column('buyerCount', String(length=20)),
)

count_manager = Table('count_manager', post_meta,
    Column('countID', String(length=20), primary_key=True, nullable=False),
    Column('countPassword', String(length=20)),
    Column('countType', Integer),
    Column('countStatus', Integer),
    Column('countProperty', Float),
)

item_manager = Table('item_manager', post_meta,
    Column('itemID', String(length=20), primary_key=True, nullable=False),
    Column('itemName', String(length=50)),
    Column('seller', String(length=20)),
    Column('itemType', Integer),
    Column('itemStatus', Integer),
)

order_manager = Table('order_manager', post_meta,
    Column('orderID', String(length=20), primary_key=True, nullable=False),
    Column('orderName', String(length=50)),
    Column('buyer', String(length=20)),
    Column('seller', String(length=20)),
    Column('orderStatus', Integer),
    Column('orderTime', Time),
)

seller = Table('seller', post_meta,
    Column('sellerID', String(length=20), primary_key=True, nullable=False),
    Column('sellerName', String(length=50)),
    Column('sellerCount', String(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['buyer'].create()
    post_meta.tables['count_manager'].create()
    post_meta.tables['item_manager'].create()
    post_meta.tables['order_manager'].create()
    post_meta.tables['seller'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['buyer'].drop()
    post_meta.tables['count_manager'].drop()
    post_meta.tables['item_manager'].drop()
    post_meta.tables['order_manager'].drop()
    post_meta.tables['seller'].drop()
