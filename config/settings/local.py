from .base import *  # noqa
from pathlib import Path

DEBUG = True

BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES[0]["DIRS"] = [
    BASE_DIR / "templates",
]

AUTH_PASSWORD_VALIDATORS = []

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/home/"
LOGOUT_REDIRECT_URL = "/login/"
