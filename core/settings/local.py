from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
