#Here is where we route the path from the websocket to the link of the room

#We import re_path from django urls
from django.urls import re_path

#We also import the ChatConsumer from the consumer
from .consumers import ChatConsumer

#Changing the Room name acquired from the name of the room to the link
websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
]