# !/usr/bin/env python
# coding=utf8
# Author: quheng
import sys
sys.path.append("..")

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from manager import db
import os.path
# print SQLALCHEMY_MIGRATE_REPO
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    # print api
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
db.create_all()


import sys
sys.path.append("..")


from manager import db, app
from admin.admin_models import Role
from admin.admin_models import Manager
from flask_security import SQLAlchemyUserDatastore
from flask_security.utils import encrypt_password
import key
with app.app_context():
	user_role = Role(name='user')
	super_user_role = Role(name='superuser')
	db.session.add(user_role)
	db.session.add(super_user_role)
	db.session.commit()
	user_datastore = SQLAlchemyUserDatastore(db, Manager, Role)
	test_user = user_datastore.create_user(\
		first_name=key.MANAGER_NAME,\
		email=key.MAIL_USERNAME,\
		password=encrypt_password(key.MANAGER_PASSWORD),\
		roles=[user_role, super_user_role])
	db.session.commit()