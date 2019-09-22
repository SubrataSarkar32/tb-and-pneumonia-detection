import logging
import os
from app.config_common import *


# DEBUG can only be set to True in a development environment for security reasons
DEBUG = False

# Secret key for generating tokens
SECRET_KEY = 'secret_key'

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'passwordly')

# Database choice
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'yourmail@gmail.com'
MAIL_PASSWORD = 'password'
ADMINS = ['yourname@gmail.com']

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

LOG_LEVEL = logging.DEBUG
LOG_FILENAME = 'activity.log'
LOG_MAXBYTES = 1024
LOG_BACKUPS = 2
TIMEZONE = 'Asia/Kolkata'
PEOPLE_FOLDER = os.path.join('static', 'xrayimgs')
UPLOAD_FOLDER = os.path.join('flaskSaaS-master','app','static', 'xrayimgs')
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['jpg','jpeg','png']
