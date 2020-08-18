#Here the model is being created

#We import the user models from django contrib
from django.contrib.auth import get_user_model
#We also import from the database the models
from django.db import models

#We assign the User to the gotten user model
User = get_user_model()

class Message(models.Model):
    #Assigning the author, content and timestamp of the messages
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    #Getting the username 
    def __str__(self):
        return self.author.username

    #Getting the last 10 messages and displaying them
    #The last 10 messages are stored and displayed
    #They are displayed in order of time
    #Modifying to receive and show the last 5 messages only
    #To show 10 messages, change to .all()[:5]
    def last_10_messages():
        return Message.objects.order_by('-timestamp').all()[:5]