from tutorial.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['api']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '!dlatl00',
        'HOST': 'database',
        'PORT': '5432',
    }
}
