import os


"""
Django settings for oxus project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from datetime import timedelta


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u^-d89lk^8r9_8fu#$gg^8@xlzi_%$6^*_srd9a2_g69q0v#yk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'users.User'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'terminals.apps.TerminalsConfig',

    'rest_framework',
    'django_filters',
    'dynamic_rest',
    'rosetta',

    'helpdesk.apps.HelpdeskConfig',
    'request_credit.apps.RequestCreditConfig',
    'division.apps.DivisionConfig',
    'credits.apps.CreditsConfig',
    'corsheaders',
    'users.apps.UsersConfig',
    'black_list',
    'reports',
    'scan',
    'accounting.apps.AccountingConfig',
    'scoring',
    'common',  # common must be last, because have checks in app ready
    'customer.apps.CustomerConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.WhoDidItMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'common.middleware.UserInterfaceLanguage.LocaleMiddleware',
]

ROOT_URLCONF = 'oxus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oxus.wsgi.application'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'common.helpers.exception_handler.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'auth.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'dynamic_rest.renderers.DynamicBrowsableAPIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('ru', 'Русский'),
    ('en', 'English'),
    ('tg', 'Точики'),
]
LOCALE_PATHS = (BASE_DIR + 'locale/', )

TIME_ZONE = 'Asia/Ashgabat'

USE_I18N = True

USE_TZ = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = 'static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_HEADERS = ["*"]
# CORS_ALLOWED_ORIGINS = ["*"]
# CORS_ALLOW_METHODS = ["*"]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=720),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
}

FILE_UPLOAD_DIR = 'upload'

FILE_NAME_LENGTH = 255

try:
    from .settings_local import *  # noqa: Skip autoflake
except ModuleNotFoundError:
    from warnings import warn
    warn("oxus.settings_local.py was not found, using default settings")