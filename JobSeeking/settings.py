"""
Django settings for JobSeeking project.

Generated by 'django-admin startproject' using Django 2.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from decouple import config,Csv
import cloudinary
import cloudinary.uploader
import cloudinary.api

MODE = config("MODE", default="dev")
SECRET_KEY = config('SECRET_KEY')

# development
if config('MODE') == "dev":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': '',
        }

    }
# production
else:
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL')
        )
    }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
# DATABASES = { 'default': dj_database_url.config() }

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-n3=(*3k)zjzjkz^mlb*)1iknt20y*pla7i3e^kkdl0!gm(qy9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'seekapp',
    'crispy_forms',
    'bootstrap4',
    'cloudinary',
    

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'JobSeeking.urls'

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

WSGI_APPLICATION = 'JobSeeking.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_REDIRECT_URL = 'profile'
# LOGOUT_REDIRECT_URL = 'login'

cloudinary.config( 
  cloud_name = "dxszxm1de", 
  api_key = "425287129295112", 
  api_secret = "G2q33r2xhFA47cpvXLhhHWwTNPk" 
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dxszxm1de',
    'API_KEY': '425287129295112',
    'API_SECRET': 'G2q33r2xhFA47cpvXLhhHWwTNPk'
}


CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'





AUTH_USER_MODEL = 'seekapp.User'



JAZZMIN_SETTINGS = {
      # title of the window (Will default to current_admin_site.site_title if absent or None)
   "site_title": "Jobseekeers",
# Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "snagjobs",
     # Welcome text on the login screen
    "welcome_sign": "Welcome to the Snagjobs",
    # Copyright on the footer
    "copyright": "Snagjobs ltd @2022",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",
     "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/mary-wan", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "seekapp"},
    ],
     "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "custom_links": {
    "books": [{
        
             
    }]
},
}

#adding config
cloudinary.config( 
  cloud_name = 'the-collector', 
  api_key =  '385692492331583', 
  api_secret = 'wpPzGYYSWBJ_4NCwwSEC0YUMSO8'
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'the-collector',
    'API_KEY': '385692492331583',
    'API_SECRET': 'wpPzGYYSWBJ_4NCwwSEC0YUMSO8'
}


django_heroku.settings(locals())