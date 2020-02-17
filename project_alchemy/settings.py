import os
import re

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "JHGFVBGFVjgvhgjvhkj,bjkjnm")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv("NODEBUG") is None else False

# TODO: Change your domain names here.
ALLOWED_HOSTS = ["*"]

# TODO: Change the default "from" email here.
DEFAULT_FROM_EMAIL = "me@mydomain.com"

# Application definition

INSTALLED_APPS = [
    "rest_framework",
    "drf_yasg",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "project_alchemy.middleware.StatsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project_alchemy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "project_alchemy.context_processors.settings",
            ]
        },
    }
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.DjangoModelPermissions"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_FILTER_BACKENDS": ["rest_framework.filters.OrderingFilter"],
    "PAGE_SIZE": 10,
}

TEMPLATE_STRING_IF_INVALID = "VARIABLE UNDEFINED: %s"

WSGI_APPLICATION = "project_alchemy.wsgi.application"

AUTH_USER_MODEL = "main.User"

# Adjust this to taste.
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# Keep connections in the pool for an hour.
CONN_MAX_AGE = 60 * 60

if os.getenv("DATABASE_URL"):
    # Running under Dokku.
    USER, PASSWORD, HOST, PORT, NAME = re.match(  # type: ignore
        r"^postgres://(?P<username>.*?)\:(?P<password>.*?)\@(?P<host>.*?)\:(?P<port>\d+)\/(?P<db>.*?)$",
        os.getenv("DATABASE_URL", ""),
    ).groups()

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": NAME,
            "USER": USER,
            "PASSWORD": PASSWORD,
            "HOST": HOST,
            "PORT": int(PORT),
        }
    }

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": os.getenv("REDIS_URL", "") + "/1",
            "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        }
    }

    SESSION_CACHE_ALIAS = "default"
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_COOKIE_AGE = 365 * 24 * 60 * 60
    SESSION_COOKIE_SECURE = True
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

if os.getenv("EMAIL_URL", ""):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT = re.match(  # type: ignore
        r"^email://(?P<username>.*)\:(?P<password>.*?)\@(?P<host>.*?)\:(?P<port>\d+)\/?$",
        os.getenv("EMAIL_URL", ""),
    ).groups()
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        }
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "_static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

try:
    from .local_settings import *  # noqa
    from .local_settings import LOCAL_INSTALLED_APPS, LOCAL_MIDDLEWARE
except ImportError:
    pass

try:
    INSTALLED_APPS += LOCAL_INSTALLED_APPS
except:  # noqa
    pass

try:
    MIDDLEWARE += LOCAL_MIDDLEWARE
except:  # noqa
    pass
