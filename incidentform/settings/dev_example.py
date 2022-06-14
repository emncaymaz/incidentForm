from .common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# if you wat to use testing mail sending
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SECRET_KEY = 'secret'

DEBUG = True

ALLOWED_HOSTS = []


LOGIN_URL = urls.reverse_lazy('sso-dev')
