from .common import *
import dj_database_url
import os 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['dejibuy-prod.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}