#DJANGO CHANNELS

Using django channels to build a chat application.
The server is built using django and text messages stored in an sqlite database
To run:
    "   json
        pip install -r requirements.txt
        python manage.py runserver
    "
	

Then open the localhost at;
	http://1227.0.0.1/8000/admin

Log in with the user credentials then proceed to the chat page in the link below
	http://127.0.0.1/8000/chat
In the chat page, key in the name of the room you wish to join and press enter. 
This will take you to the room page and if there are other users you can join and chat with them.

The requirements of the application are as follows;
I have used: Memurai instead of redis since redis is no longer supported on windows.

