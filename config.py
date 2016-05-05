import key

CSRF_ENABLED = True
SECRET_KEY = 'softwareA'

# database
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True


# mail server settings
MAIL_SERVER = 'smtp.sina.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = key.MAIL_USERNAME
MAIL_PASSWORD = key.MAIL_PASSWORD

# administrator list
ADMINS = ['494862190@qq.com']
