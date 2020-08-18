"""
WSGI config for MyApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""
#importing OS
import os

#importing the wsgi application from django wsgi
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyApp.settings')

#Getting the application
application = get_wsgi_application()
