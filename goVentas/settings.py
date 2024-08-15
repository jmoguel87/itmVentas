import os
from pathlib import Path
from pythonjsonlogger import jsonlogger

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+we5g3*bxceyp_or@&uyefe@z8%m!avpxkc5$(dhgh2xqs=cr5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.clients',
    'apps.core',
    'apps.params',
    'apps.articles'
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

ROOT_URLCONF = 'goVentas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
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

WSGI_APPLICATION = 'goVentas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASE_ROUTERS = [
    'apps.core.dbrouters.ControlDBRouter',    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb', 
        'USER':'djangodbuser',
        'PASSWORD':'64lgDAdr28NbvED%zI1wE$9*oAc3Sgqn', 
        'HOST': 'localhost', 
        'PORT': '5432',
    },
    'clients':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gocontroldb', 
        'USER':'gocontroluserdb',
        'PASSWORD':'GBInf^r51Jz7gXtIMntfcoM9r03lL#ET', 
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEXTBOXMAXLENGTH=100
RFCMAXLENGTH=100

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] = int(record.created * 1000) 

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{message}',
            'datefmt' : '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'verbose': {
            'format': '{levelname} | {name} | {asctime},{msecs} | {process}:{threadName} | {pathname}-{module}:{lineno} - {funcName} | {message}',
            'datefmt' : '%Y-%m-%d %H:%M:%S',
            'style': '{',
        },
        'complex': {
            '()': CustomJsonFormatter,
            'format': '%(mac)s | %(source_ip)s | %(asctime)s | %(timestamp)s | %(request)s | %(user_agent)s | %(levelname)s | %(name)s | %(filename)s | %(pathname)s:%(lineno)s - %(funcName)s | %(module)s:%(lineno)d | %(process)d:%(threadName)s:%(thread)s | %(message)s',
        },
    },
    'handlers': {
        'TradesLogfile': {      # Output logs to the terminal
            'level': 'INFO',
            #'filters': ['new_add'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'simple',
            'filename': 'logs/tradesKrakenApp.log',
            'when': 'D', # Days
            "interval": 1, # Every One Hour
            "backupCount": 20,  # number of backup files to keep: 20 Days
        },
        'SpreadsLogfile': {      # Output logs to the terminal
            'level': 'INFO',
            #'filters': ['new_add'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'simple',
            'filename': 'logs/spreadsKrakenApp.log',
            'when': 'H', # Days
            "interval": 1, # Every One Hour
            "backupCount": 480,  # number of backup files to keep: 20 Days
        },
        'MapLogfile': {      # Output logs to the terminal
            'level': 'INFO',
            #'filters': ['new_add'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'simple',
            'filename': 'logs/mapKrakenApp.log',
            'when': 'D', # Days
            "interval": 1, # Every One Day
            "backupCount": 20,  # number of backup files to keep: 20 Days
        },
        'ErrorLogfile':{
            'level': 'ERROR',
            #'filters': ['new_add'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'complex',
            'filename': 'logs/errorKrakenApp.log',
            'when': 'D', # Days
            "interval": 1, # Every One Day
            "backupCount": 20,  # number of backup files to keep: 20 Days
        },
    },
    'loggers': {
        'TradesLog': {      
            'handlers': ['TradesLogfile'],
            'level': 'INFO',
            'propagate': True,
        },
        'SpreadsLog': {      
            'handlers': ['SpreadsLogfile'],
            'level': 'INFO',
            'propagate': True,
        },
        'MapLog': {      # Defines a name django A new logger
            'handlers': ['MapLogfile'],              # It can output log to terminal and file at the same time
            'level': 'INFO',                      # The lowest log level that the logger receives
            'propagate': True,                   # Whether to inherit the log Information ,0: no 1: yes
        },
        'ErrorLog': {
            'handlers': ['ErrorLogfile'],
            'level': 'ERROR',
            'propagate': True,
        }
    },
}