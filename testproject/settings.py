# -*- coding: utf-8 -*-

import os

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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3')
    }
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
