"""
Django settings for idb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h#tb420ho@#ob%u&a=rc&t2e6*m!4s-e-m538zzywi9k^8xcz@'
if 'test' in sys.argv:
    DATABASES = {
        'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/pa-test.db'
        }
    }
else :
    DATABASES = {
    'default':
    {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbclbiroo6chk4',
        'HOST': 'ec2-54-204-37-113.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'mlsprslbyogyne',
        'PASSWORD': 'RWzrOqD9IWPhEQujKh2wkYd59J'
    }
}

SITE_ID=1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'OperationRepo',
    'rest_framework'

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'idb.urls'

WSGI_APPLICATION = 'idb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#   'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'deso8mn255r48h',
#     'HOST': 'ec2-54-197-246-197.compute-1.amazonaws.com',
#     'PORT': 5432,
#     'USER': 'mrptrwcgqdpavw',
#     'PASSWORD': 'exLhPO8jMr2-7qGT9yYiavmLQu'
#   }
# }

#DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Template Path
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'templates/OperationRepo')
)

