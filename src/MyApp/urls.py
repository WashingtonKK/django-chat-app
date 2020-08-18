#We import admin from django contrib and path from urls
from django.contrib import admin

#We are importing the path we created in the urls file
from django.urls import path, include

#The patterns of the URLS 
urlpatterns = [
    #Admin path to log in
    path('admin/', admin.site.urls),

    #Converting the urls to a path
    path('chat/', include('chat.urls', namespace='chat')),
]
