from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "spotify.apanel.top",
    "http://spotify.apanel.top",
    "https://spotify.apanel.top",
    "http://localhost:3000",
    "http://localhost:5000",
    "https://react-spotify-app-red.vercel.app",
]

CORS_ALLOWED_ORIGINS = [
    "http://spotify.apanel.top",
    "https://spotify.apanel.top",
    "http://localhost:3000",
    "http://localhost:5000",
    "https://react-spotify-app-red.vercel.app",
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"(?:https?://)?react-spotify-app-red\.vercel\.app:(\d+)",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
