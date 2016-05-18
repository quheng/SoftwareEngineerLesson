from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
seller = Table('seller', post_meta,
    Column('sellerID', String(length=20), primary_key=True, nullable=False),
    Column('sellerPhoto', String(length=100)),
    Column('sellerName', String(length=50)),
    Column('sellerCount', String(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['seller'].columns['sellerPhoto'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['seller'].columns['sellerPhoto'].drop()
