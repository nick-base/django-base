# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import os
from settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'web/db.sqlite3'),
    }
}
