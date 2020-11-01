"""
Django settings for TravelGuide project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from __future__ import absolute_import
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APP_HOME=BASE_DIR

SECRET_KEY =  'ffhjfgghghhfhfghfklhrtrtrttrrtrtjhdfgghlsnjvv%9h@m=hz@jid=s7*t*8r73'
DEBUG=True
ALLOWED_HOSTS = ['*']

MEDIA_ROOT='static/storage/'
MEDIA_URL = '/media/'
#statics
STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

STRIPE_API_KEY="sk_test_mg2XfC6BiICVWq4HX4FTUR5y00YTeD2oYR"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bo',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

POSTGRESQL_ADDON_URI = os.getenv("POSTGRESQL_ADDON_URI")
POSTGRESQL_ADDON_PORT = os.getenv("POSTGRESQL_ADDON_PORT")
POSTGRESQL_ADDON_HOST = os.getenv("POSTGRESQL_ADDON_HOST")
POSTGRESQL_ADDON_DB = os.getenv("POSTGRESQL_ADDON_DB")
POSTGRESQL_ADDON_PASSWORD = os.getenv("POSTGRESQL_ADDON_PASSWORD")
POSTGRESQL_ADDON_USER = os.getenv("POSTGRESQL_ADDON_USER")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  #'django.db.backends.mysql',
        'NAME': POSTGRESQL_ADDON_DB,
        'USER': POSTGRESQL_ADDON_USER,
        'PASSWORD': POSTGRESQL_ADDON_PASSWORD,
        'HOST': POSTGRESQL_ADDON_HOST,
        'PORT': POSTGRESQL_ADDON_PORT,
        'CONN_MAX_AGE': 1200,
    }
}

#Logging
U_LOGFILE_SIZE = 10 * 1024 * 1024
U_LOGFILE_COUNT = 7
fileName="django.log"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(MEDIA_ROOT, fileName),
            'maxBytes': U_LOGFILE_SIZE,
            'backupCount': U_LOGFILE_COUNT,
            'formatter': 'verbose'
        },
        'celerylog': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(MEDIA_ROOT, fileName),
            'maxBytes': U_LOGFILE_SIZE,
            'backupCount': U_LOGFILE_COUNT,
            'formatter': 'verbose'
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
        'bo': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    }
}

X_FRAME_OPTIONS = 'ALLOWALL'
CORS_ORIGIN_ALLOW_ALL=True
 

ROOT_URLCONF = 'stripecheckout.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            BASE_DIR,
            os.path.join(BASE_DIR, 'templates')
        ],
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.debug',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
            ],

        },
    },
]


WSGI_APPLICATION = 'stripecheckout.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

FIXTURE_DIRS = (
   '/fixtures/',
)

