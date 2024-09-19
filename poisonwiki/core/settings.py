"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# ------------------------------
# Imports and Environment Setup
# ------------------------------
from pathlib import Path
import os
import environ
import dj_database_url
from django.contrib import messages
from django.core.management.utils import get_random_secret_key

# ------------------------
# Project Paths and Files
# ------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# Setting up django-environ
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR / ".env")


# ------------------------
# Static Files Configuration
# ------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_ROOT = BASE_DIR / "media_root"
MEDIA_URL = "/media/"


# ------------------------
# Application Configuration
# ------------------------
INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup.apps.CleanupConfig",
    "authtools",
    "ckeditor",
    "crispy_forms",
    "crispy_bootstrap5",
    "view_breadcrumbs",
    "active_link",
    "localflavor",
    "django_seed",
    "django_filters",
    "import_export",
    "django_htmx",
    "corsheaders",
    "extra_views",
    "django_extensions",
    "pwa",
    "rest_framework",
    "django_minify_html",
    "sorl.thumbnail",
    "accounts",
    "poisons",
]


# ------------------------
# Middleware Configuration
# ------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
    "django_minify_html.middleware.MinifyHtmlMiddleware",
]


# ------------------------
# Template Related Settings
# ------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap5-responsive.html"
MESSAGE_TAGS = {
    messages.DEBUG: "bg-light",
    messages.INFO: "text-white bg-primary",
    messages.SUCCESS: "text-white bg-success",
    messages.WARNING: "text-dark bg-warning",
    messages.ERROR: "text-white bg-danger",
}
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
THUMBNAIL_PRESERVE_FORMAT = True
CKEDITOR_UPLOAD_PATH = "pannel_uploads/"

CKEDITOR_CONFIGS = {
    "default": {
        # 'toolbar': None, #You can change this based on your requirements.
        "width": "auto",
    },
}
# ------------------------
# PWA Configuration
# ------------------------
PWA_SERVICE_WORKER_PATH = BASE_DIR / "static/assets/js/serviceworker.js"
PWA_APP_NAME = "PoisonWiki"
PWA_APP_DESCRIPTION = "All about poisons and toxins"
PWA_APP_THEME_COLOR = "#0A0302"
PWA_APP_BACKGROUND_COLOR = "#ffffff"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "portrait"
PWA_APP_START_URL = "poisons:list"
PWA_APP_STATUS_BAR_COLOR = "default"
PWA_APP_ICONS = [
    {
        "src": "/static/assets/imgs/LogoPoison.png",
        "sizes": "256x256",
        "purpose": "maskable",
    },
    {
        "src": "/static/assets/imgs/LogoPoison.png",
        "sizes": "256x256",
    },
]
PWA_APP_SPLASH_SCREEN = [
    {
        "src": "/static/images/icons/splash-640x1136.png",
        # "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
    }
]
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "pt-BR"
# PWA_APP_SHORTCUTS = [
#     {
#         'name': 'Shortcut',
#         'url': '/target',
#         'description': 'Shortcut to a page in my application'
#     }
# ]
PWA_APP_SCREENSHOTS = [
    {
        "src": "/static/assets/imgs/timeline.jpg",
        "sizes": "1074x2100",
        "type": "image/jpg",
    },
    {
        "src": "/static/assets/imgs/history_card_open.jpg",
        "sizes": "1071x2100",
        "type": "image/jpg",
    },
    {
        "src": "/static/assets/imgs/history_card_closed.jpg",
        "sizes": "1079x2100",
        "type": "image/jpg",
    },
]


# ------------------------
# Crispy Forms Configuration
# ------------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# ------------------------
# Security Related Settings
# ------------------------
SECRET_KEY = env("SECRET_KEY", default=get_random_secret_key())
DEBUG = env("DEBUG")
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"] + env("ALLOWED_HOSTS").split(" ")
CSRF_TRUSTED_ORIGINS = [
    "http://*localhost:8000",
    "http://*0.0.0.0:8000",
    "http://*127.0.0.1:8000",
    "http://*localhost",
    "http://*0.0.0.0",
    "http://*127.0.0.1",
] + env("CSRF_TRUSTED_ORIGINS").split(" ")
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ------------------------
# CORS Configuration
# ------------------------
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
SECURE_CROSS_ORIGIN_OPENER_POLICY = None


# ------------------------
# User Authentication Configuration
# ------------------------
AUTH_USER_MODEL = "accounts.User"
LOGIN_REDIRECT_URL = "poisons:list"
LOGIN_URL = "accounts:sign_in"
LOGOUT_REDIRECT_URL = LOGIN_URL
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# ------------------------
# Email Backend Configuration
# ------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ------------------------
# Password Validation
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ------------------------
# Internationalization Settings
# ------------------------
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
DATE_FORMAT = "d/m/Y"
TIME_FORMAT = "H:M:S"
DATETIME_FORMAT = "d/m/Y, H:M"
USE_I18N = True
USE_TZ = False
USE_L10N = False


# ------------------------
# Main URLs Location
# ------------------------
ROOT_URLCONF = "core.urls"

# ------------------------
# WSGI Configuration
# ------------------------
WSGI_APPLICATION = "core.wsgi.application"

# ------------------------
# Database Configuration
# ------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
db_from_env = dj_database_url.config(conn_max_age=500, conn_health_checks=True)
DATABASES["default"].update(db_from_env)

# ------------------------
# Default Primary Key Field Type
# ------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ------------------------
# Logging Configuration
# ------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


# ⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀
# ⠀⠀⠀⠀⠀⣼⢻⠈⢑⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢎⠁⠉⣻⡀
# ⠀⠀⠀⠀⠀⡇⠀⠁⢙⣿⣮⢲⠀⠀⠀⠀⠀⠀⠀⢠⣾⣟⠀⠸⢫⡇
# ⠀⠀⠀⠀⠀⣧⢀⠀⠘⣷⣿⠆⠀⠐⠘⠿⠓⠀⠀⢾⣧⠃⠀⠐⣼
# ⠀⠀⠀⠀⠀⠘⣇⢰⣶⠛⣁⣐⣷⣦⠐⢘⣼⣷⣂⡀⠛⢽⣆⣸⠁
# ⠀⠀⠀⠀⠀⣚⣾⡿⢡⣴⣿⣿⣿⣿⠇⠸⣿⣿⣿⣿⣶⡄⠾⣷⣟⡀
# ⠀⠀⠀⠀⠘⣻⠇⣲⡿⠟⠋⠉⠉⢿⠰⠆⡿⠋⠉⠙⠿⣿⣆⡻⣿⣓
# ⠀⠀⠀⣰⢿⣷⠞⢩⡤ ★ ⡀⣀⠀⡀⣠⡀★⡀⢤⣨⠛⢷⣿⣭⠃
# ⠀⠀⠀⣶⠟⠁⠶⠡⠄⠀⠀⣠⣾⡟⠘⠃⢻⣿⣌⠿⠾⠟⢺⣷⣏⠻⣷
# ⠀⠀⠘⠿⣔⠺⢿⣧⡤⠀⢰⣿⣿⡀⠘⠀⢀⣿⣿⡆⡂⠀⡈⠡⠜⣙⣿⠇
# ⠀⠀⠀⠐⠻⢿⣶⣅⢀⠐⠀⠙⣒⡃⡀⠄⢘⠉⠋⠁⠆⢀⢼⣿⣿⡟⠋⠁
#          github.com/Iah-Uch
