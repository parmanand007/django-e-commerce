from .base import *

DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['ip-address', 'www.your-website.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': config('DB_NAME'),
    #     'USER': config('DB_USER'),
    #     'PASSWORD': config('DB_PASSWORD'),
    #     'HOST': config('DB_HOST'),
    #     'PORT': ''
    # }
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'railway'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'gf2-6C1AE5cA1GAd-AdedA-61dbCaDbb'),
        'HOST': os.environ.get('POSTGRES_HOST', 'roundhouse.proxy.rlwy.net'),  # Adjusted to use 'DB_HOST'
        'PORT': os.environ.get('POSTGRES_PORT', '38810'),
    }
}

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')