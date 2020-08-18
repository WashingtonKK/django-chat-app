#Creating the views

#Since we want several users, we will import login_required to add the login_requirements
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe

#We import JSON
import json

#We redirect the request to the chat file named index.html
#The file is stored in the folder called chat
def index(request):
    return render(request, 'chat/index.html', {})

#Working on the login 
#It requires a log-in in order to access the room
@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })