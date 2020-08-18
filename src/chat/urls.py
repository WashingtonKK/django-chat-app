#Generating the urls

#Imports, path, re_path, index and rooms
from django.urls import path, re_path

#The index and rooms are imported from the views.py file
from .views import index, room

#Configuring the name of the app
app_name = 'chat'

#Generating the path and url
urlpatterns = [
    path('', index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
