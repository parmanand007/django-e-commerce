from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','localhost']

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True

TIME_ZONE = 'UTC'
USE_TZ = False

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'railway'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'eDAd-2Fdc11F*Fe*a-ba5ec*Fb4cbD66'),
        'HOST': os.environ.get('POSTGRES_HOST', 'roundhouse.proxy.rlwy.net'),  # Adjusted to use 'DB_HOST'
        'PORT': os.environ.get('POSTGRES_PORT', '10364'), 
    }
}

STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
