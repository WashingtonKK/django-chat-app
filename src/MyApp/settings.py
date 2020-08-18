#Here we have the app settings

import os

# THe paths should be built inside the project in this manner: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Whwn in prroduction, the secret key is to be kept in secret
SECRET_KEY = '9nneu#^7_aai*(#(6_qiihu-^k-+%a86&vjh=_i9#(c4^8s51n'

# When in production, turn off Debug mode
DEBUG = True

#Allowed hosts
ALLOWED_HOSTS = []



#Here we give the list of installed apps
#The other apps come by default except channels and chat
#chat is our app, the one we created
#channels is the framework we will be using
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'chat'
]

#Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#Configuring the URL of the root
ROOT_URLCONF = 'MyApp.urls'

#Here we will specify any templates we have and are using
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#The default comes with a WSGI application, however since we are using ASGI we will add it also
WSGI_APPLICATION = 'MyApp.wsgi.application'
ASGI_APPLICATION = "MyApp.routing.application"

#The layer of the channel we used redis
CHANNEL_LAYERS = {
    'default': {
        #Configuring the backend as redis
        'BACKEND': 'channels_redis.core.RedisChannelLayer', 
        #Redis runs on port 6379
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


#For our database we will use SQLITE3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#Validating the password input
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization of time

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
#Defining the static that is used for imports to avoid the room name
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]