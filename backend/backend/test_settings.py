from .settings import *  # NOQA


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth_vk.hashers.MD5PasswordHasher',
)

DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
