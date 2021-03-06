import os

# Misc

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Forms

CSRF_ENABLED = True
SECRET_KEY = '<REPLACE WITH REAL VALUE>'

# OpenID

OPENID_PROVIDERS = [
  { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
  { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
  { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
  { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
  { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# Mail server settings

MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['tolowercase@gmail.com']
