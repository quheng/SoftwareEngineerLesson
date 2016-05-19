from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
count_manager = Table('count_manager', pre_meta,
    Column('countID', VARCHAR(length=20), primary_key=True, nullable=False),
    Column('countPassword', VARCHAR(length=20)),
    Column('countType', INTEGER),
    Column('countStatus', INTEGER),
    Column('countProperty', FLOAT),
)

item_manager = Table('item_manager', pre_meta,
    Column('itemID', VARCHAR(length=20), primary_key=True, nullable=False),
    Column('itemName', VARCHAR(length=50)),
    Column('seller', VARCHAR(length=20)),
    Column('itemType', INTEGER),
    Column('itemStatus', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['count_manager'].drop()
    pre_meta.tables['item_manager'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['count_manager'].create()
    pre_meta.tables['item_manager'].create()
