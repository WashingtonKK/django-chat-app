#We import admin
from django.contrib import admin

#Import message from the models class
from .models import Message

#The message is registered in the site
admin.site.register(Message)