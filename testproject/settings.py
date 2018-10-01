# -*- coding: utf-8 -*-

import os

from decouple import config
import dj_database_url
from django.utils.translation import ugettext_lazy as _


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
FPR_PATH = os.path.abspath(os.path.join(PROJECT_PATH, '../fpr'))

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'django_forms_bootstrap',

    'fpr',
]

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('fr', _('French')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('pt-br', _('Brazilian Portuguese')),
    ('ja', _('Japanese')),
    ('sv', _('Swedish')),
]

LOCALE_PATHS = [
    os.path.join(PROJECT_PATH, 'locale'),
    os.path.join(FPR_PATH, 'locale'),
]

ROOT_URLCONF = 'testproject.urls'

TIME_ZONE = 'UTC'

DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': (
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages"
            )
        },
        'DIRS': (os.path.join(PROJECT_PATH, 'templates'), '')
    },
]

SECRET_KEY = 'empty'

DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=dj_database_url.parse,
        default='sqlite:///{}'.format(os.path.join(PROJECT_PATH, 'db.sqlite3')),
    ),
}

# Ensure that the strict mode is enabled when using MySQL. This forces MySQL to
# return an error instead of a warning which helps us to find incompatibilities
# with the strict mode even when using MySQL 5.5 - the one provided by
# Travis CI or frequently deployed in Ubuntu Trusty.
if DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
    DATABASES['default']['OPTIONS'] = {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES';"
                        "SET innodb_strict_mode=1;",
    }

DATABASE_SUPPORTS_TRANSACTIONS = True

USE_TZ = True

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
