"""
Django settings for Eshop project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '5bad1g&sjplz#xd@kz0d=ej%xw(n&_6ng#)()np9(vl)lw_h8u'
SECRET_KEY = os.environ.get('SOME_SECRET_KEY', '5bad1g&sjplz#xd@kz0d=ej%xw(n&_6ng#)()np9(vl)lw_h8u')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval(os.environ.get('DEBUG_MODE', 'True'))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [] if DEBUG else ['78.155.219.170']


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'import_export',
    'djcelery_email',
    'mptt',
    'landing',
    'orders',
    'loginsys',
    'userprofile',
    # 'haystack',
    'products',
    'cart',
    # 'paypal.standard.ipn',
    # 'payment',
    'discount',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Eshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                # 'orders.context_processors.getting_basket_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'Eshop.wsgi.application'

MPTT_ADMIN_LEVEL_INDENT = 20
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'eshop_db',
            'USER': 'denis',
            'PASSWORD': '12345678',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'db1',
            'USER': 'django_shop',
            'PASSWORD': 'django_shop12345',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

DATE_FORMAT = 'd E Y'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static", "static_dev"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "static/")#, "static_dev")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

CART_SESSION_ID = 'cart'

# Email
ADMINS = (
    ('Denis Balyasnikov', 'bda2291@mail.ru'),
)

MANAGERS = ADMINS

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'balyasnikovdenis22@gmail.com'
EMAIL_HOST_PASSWORD = 'ltybcbrhbcnbyf22'

FROM_EMAIL = 'notreply@russianprograms'
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'

# for import-export excel data
IMPORT_EXPORT_USE_TRANSACTIONS = True

# WHOOSH_INDEX = os.path.join(os.path.dirname(__file__), "whoosh/")

# Uncomment for elasticsearch

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 12
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': 'http://127.0.0.1:9200',
#         'INDEX_NAME': 'haystack',
#         # 'INCLUDE_SPELLING': True,
#     },
# }

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'