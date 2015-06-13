import os

PROJECT_ROOT = os.path.dirname(__file__)

DEBUG = True
SECRET_KEY = 'hyA24C7HwxfThde4r56nEyTeuXeyTh'
ROOT_URLCONF = 'djangoproject.urls'

TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, 'templates')]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public')

STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, 'static')]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_dark_theme'
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'drf_dark_theme.renderers.MoonshineBrowsableAPIRenderer',
    )
}