# Flask is web-development micro framework
# It doesn't have many features. Most of the things requires extensions. Following are the two major features
# Jinja 2: It is template engine
# Werkzeug: It provides HTTP related features

from flask import Flask
from datetime import datetime
count = 0
app = Flask(__name__)  # invoking Flask constructor with filename(application name)


@app.route("/")  # this decorator will change the function to view function
def welcome():
    return " Welcome to Flask "


@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())


@app.route("/count")
def view_count():
    global count
    count += 1
    return f"This page has been viewed {count} times"

# To run any flask application, first we need to set some environment variables in virtual environment
# FLASK_APP: With this variable we will specify the name of the flask app, don't add space around '=' character
# export FLASK_APP=my_flask_intro.py (Linux) or set FLASK_APP=my_flask_intro.py (Windows)
# FLASK_ENV: With this variable we specify our flask environment.
# export FLASK_ENV=development (linux) or set FLASK_ENV=development (windows)
# It will enable features for development like debugger
# To the run the project we need to use flask run command, by default it will open the application on port 5000
# control flow of application is dictated by incoming HTTP request

# Following shows, how flask determines entry for each URL and its corresponding function
# >>> import my_flask_intro
# >>> my_flask_intro.app.url_map
# Map([<Rule '/count' (OPTIONS, GET, HEAD) -> view_count>,
#  <Rule '/date' (OPTIONS, GET, HEAD) -> date>,
#  <Rule '/' (OPTIONS, GET, HEAD) -> welcome>,
#  <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>])  # flask provide this method by default
#  we can add static files, images, json, JavaScripts using this (by creating static directory)

# We can deploy our flask application using different servers as well like gunicorn using nginx (reverse proxy)
# Deployment process on Ubuntu Linux Server
# Clone the project using Git Clone
# install all dependencies using pip3, pip3 install -r requirements.txt
# install gunicorn server, sudo apt install gunicorn3
# if we want to run multiple instances of servers or multiple applications, we should always use virtual environment
# installing gunicorn using apt will make sure we will get security updates automatically.
# installing guincorn using pip will give us latest version of gunicorn, but we need to manage updates oneself
# Run the server, gunicorn3 flashcards:app  (syntax is module_name:flask_object without .py extension)
# by default it will run on port 8000, actual websites runs on port 80, that is why we need to use nginx, which will
# run on port 80 and forward its request to gunicorn server. Due to this we need to run our gunicorn server as daemon
# gunicorn3 -D flashcards:app
# nginx configuration will be available at path /etc/nginx/sites-available, get the steps and config from the official
# gunicorn website. update server_name, and access_log location if required, then restart the service
# sudo service nginx restart
