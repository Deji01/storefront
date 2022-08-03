from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3ra(cb++b5s2qe2%z@u-ejkj11%h_vv+gkltko1orys^y!ym1d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sql8509443',
#         'HOST': 'sql8.freemysqlhosting.net',
#         'USER': 'sql8509443',
#         'PORT': 3306,
#         'PASSWORD': os.environ['PASS']
#     }
# }
