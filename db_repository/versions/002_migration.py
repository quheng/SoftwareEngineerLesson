from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
manager = Table('manager', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=255)),
    Column('last_name', String(length=255)),
    Column('email', String(length=255)),
    Column('password', String(length=255)),
    Column('active', Boolean),
    Column('confirmed_at', DateTime),
)

role = Table('role', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=80)),
    Column('description', String(length=255)),
)

roles_managers = Table('roles_managers', post_meta,
    Column('manager_id', Integer),
    Column('role_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['manager'].create()
    post_meta.tables['role'].create()
    post_meta.tables['roles_managers'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['manager'].drop()
    post_meta.tables['role'].drop()
    post_meta.tables['roles_managers'].drop()
