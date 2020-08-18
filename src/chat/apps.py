#We are configuring the apps that we have created
#The name of our application is chat

#From django apps package, we import AppConfig
from django.apps import AppConfig

#The name of the app is passed in the class ChatConfig
class ChatConfig(AppConfig):
    name = 'chat'
