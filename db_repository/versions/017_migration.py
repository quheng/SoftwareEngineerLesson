from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
complaints = Table('complaints', pre_meta,
    Column('orderID', VARCHAR(length=20), primary_key=True, nullable=False),
    Column('content', VARCHAR(length=200)),
    Column('buyer', VARCHAR(length=20)),
    Column('complaintTime', DATETIME),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['complaints'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['complaints'].create()
