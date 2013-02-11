
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': '/home/hunter/Downloads/paint/image.db',                      
        'USER': '',                     
        'PASSWORD': '',                  
        'HOST': '',                      
        'PORT': '',                     
    }
}


TIME_ZONE = 'Asia/Kolkata'


LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

SECRET_KEY = 'f%8i1h95zrbueq(v#ulx&amp;&amp;jt_xk+wo4lkydbvrvz@8hkww*k+#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    
)

ROOT_URLCONF = 'paint.urls'

WSGI_APPLICATION = 'paint.wsgi.application'

import os
PROJECT_DIR = os.path.dirname(__file__)
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, "../templates"),
	'/home/hunter/Downloads/paint/templates',

)

INSTALLED_APPS = (
    
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
