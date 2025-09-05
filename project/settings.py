from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, True), SECRET_KEY=(str, "dev-secret"), ALLOWED_HOSTS=(list, ["127.0.0.1","localhost"]))
if (BASE_DIR / ".env").exists():
    environ.Env.read_env(BASE_DIR / ".env")

DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

INSTALLED_APPS = [
    "django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles",
    "django_filters","django_htmx",
    "core","accounts","shops","catalog","cart","orders","reviews",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [{
    "BACKEND":"django.template.backends.django.DjangoTemplates",
    "DIRS":[BASE_DIR / "templates"],
    "APP_DIRS":True,
    "OPTIONS":{"context_processors":[
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
        "core.context_processors.common",
    ]},
}]

WSGI_APPLICATION = "project.wsgi.application"

DATABASES = { "default": env.db(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}") }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME":"django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME":"django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME":"django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME":"django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "uk"
TIME_ZONE = "Europe/Kyiv"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
