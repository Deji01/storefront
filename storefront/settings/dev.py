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
#         'NAME': '',
#         'HOST': '',
#         'USER': '',
#         'PORT': 3306,
#         'PASSWORD': os.environ['PASSWORD']
#     }
# }

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8001',
    'http://127.0.0.1:8001',
    'https://deji01-storefront-q7p7w7r69f65qq-8000.githubpreview.dev',
]

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}