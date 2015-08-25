"""
Django settings for composersCouch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY', 'k$s+jts3d$349yo&ojfqo1wvs!f##2w!p&h$4&qd$uz_5&a7%q')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

DEVELOPMENT = os.environ.get('DEVELOPMENT', False)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEVELOPMENT

ALLOWED_HOSTS = []


# Application definition

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'autocomplete_light',
    'jinja2',
    'pipeline',
    'social.apps.django_app.default',
    'robots',
    #'test_without_migrations',

    'accounts',
    'drchronoAPI',
    'pipeline_jinja2',
    'social_auth_drchrono',
    'utilities',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'pipeline_jinja2.middleware.MinifyHTMLMiddleware',
)

ROOT_URLCONF = 'appointment_booking_drchrono.urls'

WSGI_APPLICATION = 'appointment_booking_drchrono.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if DEVELOPMENT:
    POSTGIS_VERSION = (2, 1, 4)
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = False
    DEFAULT_FROM_EMAIL = 'testing@example.com'

    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
    MEDIA_URL = '/media/'
    PIPELINE_COMPILERS = 'pipeline.compilers.sass.SASSCompiler',
    PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

    PIPELINE_CSS = {
        'sass': {
            'source_filenames': (
              'stylesheets/theme.scss',
            ),
            'output_filename': 'stylesheets/style.min.css',
            'extra_context': {
                'media': 'screen',
            },
        },
    }

else:
    # TODO: add production settings
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DB_NAME', 'appointmentsDB'),
        'OPTIONS': {
            'options': '-c search_path=gis,public,pg_catalog'
        },
        'USER': os.environ.get('DS_USERNAME', 'postgres'),
        'PASSWORD': os.environ.get('DS_PASSWORD', 'devDatabase'),
        'HOST': os.environ.get('DS_HOSTNAME', 'localhost'),
        'PORT': os.environ.get('DS_PORT', ''),
        'ATOMIC_REQUESTS': True,
    }
}

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

TIME_ZONE = 'UCT'

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'appointment_booking_drchrono/media')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join( BASE_DIR, 'appointment_booking_drchrono/staticfiles/' )

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join( BASE_DIR, 'appointment_booking_drchrono/static' ),

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment' : 'appointment_booking_drchrono.jinja2.environment',
        }
    },
]

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

AUTHENTICATION_BACKENDS = (
    'social_auth_drchrono.backends.drchronoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.csrf',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

# over ride user defaults
ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/redirect/%s/" % u.username,
}

PIPELINE_ENABLED= True
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'


PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            'scripts/includes/jquery-1.11.0.min.js',
            'scripts/includes/fastclick.js',
            'scripts/includes/foundation.min.js',
        ),
        'output_filename': 'scripts/scripts.min.js',
        'extra_context': {
            'async': True,
        },
    }
}

ROBOTS_SITEMAP_URLS = [
    'http://www.composerscouch.com/sitemap.xml',
]

try:
    from accounts.settings import *
except ImportError:
    pass
