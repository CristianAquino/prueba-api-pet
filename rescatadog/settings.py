import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / 'staticfiles'

env = environ.Env()
environ.Env.read_env()


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    # Apps created by us
    'adoptions',
    'pet_management',
    'user_profile',
    'prueba'
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
]

ROOT_URLCONF = 'rescatadog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'rescatadog.wsgi.application'

#  if os.getenv('ENGINE').tolower() == "postgres" {
#  DATABASES = {
#  'default': {
#  'ENGINE': 'django.db.backends.postgresql_psycopg2',
#  'NAME': os.getenv('DATABASE_NAME'),
#  'USER': os.getenv('DATABASE_USER'),
#  'PASSWORD': os.getenv('DATABASE_PASSWORD'),
#  'HOST': os.getenv('DATABASE_HOST'),
#  'DATABASE_PORT': os.getenv('DATABASE_PORT'),
#  },
#  }
#  } else {
#  DATABASES = {
#  'default': {
#  'ENGINE': 'django.db.backends.sqlite3',
#  'NAME': BASE_DIR / 'db.sqlite3',
#  },
#  }
#  }

DATABASES = (
    {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': os.getenv('DATABASE_HOST'),
            'DATABASE_PORT': os.getenv('DATABASE_PORT'),
        },
    }
    if os.getenv('ENGINE', 'sqlite') == 'postgres'
    else {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
    }
)


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
