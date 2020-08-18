#The consumer that will consume the data from the chat server
#The consumer will connect to the Websocket
#Here we will handle a couple of functions
#The functions will handle sent texts, receiving texts and handling the websockets

#Importing the user Model
from django.contrib.auth import get_user_model
#Since the server will be synchronous, we import async_to_sync
from asgiref.sync import async_to_sync
#importing the websocket consumer
from channels.generic.websocket import WebsocketConsumer
#Importing JSON
import json
from .models import Message

#The variable user getst the user model
User = get_user_model()


#The class that handles our chat consumer
class ChatConsumer(WebsocketConsumer):

    #The function to fetch messages from the server
    #The function shows the last 10 messages stored and displays them
    def fetch_messages(self, data):
        #Getting the last 10 messages
        messages = Message.last_10_messages()

        #The contents of the messages is formed here
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    #Function that handles a new message input into the app
    def new_message(self, data):
        #The author of the message
        author = data['from']
        author_user = User.objects.filter(username=author)[0]

        #The author of the message and the content are created
        message = Message.objects.create(
            author=author_user, 
            content=data['message'])

        #The content of the message being formed into the content
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }

        #The message is sent
        return self.send_chat_message(content)

    #The function  to convert the messages to JSON
    #The function appends the message to an array called result
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    #The function called to add the author and content to the messages
    def message_to_json(self, message):
        #The message author, content and timestamp are returned
        return {
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    #The list of commands that are used
    #The command fetch_messages is used to display messages
    #The command new_message creates a new message
    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    #The function to connect to the websocket that conects to the room
    def connect(self):
        
        #Gets the room name
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        #Converts from Asyncronous to syncronous
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    #The function to disconnect from the websocket and eventually to the room
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )


    #The function used to receive new messages from the serrver
    def receive(self, text_data):
        #The data is loaded from JSON
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
        
    #The function that is called when the send button is pressed on the chat app
    #When the send button is sent, the text is captured here and sent to the server
    def send_chat_message(self, message):    
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    #Sending the message
    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    #The function that handles the chat messages
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))