# jokebot
A bot that displaying jokes based on button clicks and tracks button clicks by a user.

How to set up : 

1. Create virtual environment.
2. Install requirements using the command:
    pip3 install -r requirements.txt
3. Create Postgres database and change database settings in settings.py file
4. Create django and project tables using the command:
   python3 manage.py migrate


How to use:

 Joke bot can be used with or with out authentication, if not authenticated click counts won't be tracked.
 
 For tracking user click counts :
  1. Create user using command line:
       python3 manage.py createsuperuser
     Enter the required information.
  2. Go to localhost:8000/users/login/ and login, this will redirect to count screen.
  3. Go to localhost:8000/chat/ and click button to engage with the bot and get jokes
  4. Go to localhost:8000/users/click-counts/
 
 
 
