from .base import *
from .base import env


DEBUG =True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DANGO_SECRET_KEY', default='qScrYyvjBEeWPFLeGtQhOLVoPKURuRVujdvXkPwJMfpKRAelLx')


SECRET_KEY = 'django-insecure-a8pcqrgow1@2e&#%6nq!mwuqfr1ir^&0e2a9f1hjr1kyjj8imw'

ALLOWED_HOSTS = ["locahost", "0.0.0.0", "127.0.0.1"]