import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
db_password = ''

if os.environ.get('DATABASE_PASSWORD_FILE'):
    with open('/run/secrets/db_twipy_password') as f:
        db_password = f.read().strip()


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db')).format(
        user=os.environ.get('DATABASE_USER'), password=db_password,
        database=os.environ.get('DATABASE'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 8
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 25))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', None)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', None)
    MAIL_PASSWORD = os.environ.get('MAIL_USERNAME', None)
    ADMINS = ['admin@twipy.com']
    FLAG = os.environ.get('FLAG')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
