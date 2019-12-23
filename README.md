# Flask React Udacity Assessment

This is simple react-flask app for building out simple REST API. 
That consume udacity API for Courses 
With A React App to show Udacity Courses and Enroll to this courses
With A DUMMY USER
--------------

## Table of Contents

- [Swagger_Docs](#Swagger_Docs)
- [Install & Use](#install-and-use)
    - [Back-End Setup](#Back-End Setup)
        - [Using Docker](#Using Docker)
        - [Using Local Setup](#Using Local Setup)
    - [Front-End Setup](#Front-End Setup)

- [Folder Structure](#Folder Structure)
- [Others](#Others)

--------------
## Swagger_Docs
```
localhost:5000/apidocs
```

## Back-End Setup
### Using Docker
```
docker-compose up
```
- this will create and launch the app and postgres instances and create the database.
- After that every thing should be ready for the back-end .
- A POST Request API  ```http://127.0.1:5000/enrollment```
- that takes ```nanodegree_key```
and for ```udacity_user_key && status```
are being injected manually in ```Enrollment Model``` in ```__init__``` method 

```
Postgres choosed as task mentioned for me as the for the simplicity of the task
any db would work fine, i could go for SQLite as its a simple databasea that writes on a simple file
for scalability and production its a differnt story
```


### Using Local Setup

First start a postgres docker container and persist the data with a volume `flask-app-db`:

```
make start_dev_db
```

Then, start your virtual environment

```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```
Now, install the python dependencies and run the server:
```
(venv) $ pip install -r requirements.txt
(venv) $ pip install -r requirements-dev.txt
(venv) $ python manage.py recreate_db
(venv) $ python manage.py runserver
```

To exit the virtual environment:
```
(venv) $ deactivate
$
```
--------------

## Front-End Setup
- React has been choose over angular for 
> 1. the task it self is simple and doenst require the whole structure "folders, patterns, libraries" of angular
>as its gust a library not a framework, also angular has some performance issues in regarding of particular things for ex : parsing html ...
>2. Isolated components are easier to maintain

```
cd frontEnd
npm install
npm run start
```
- this will launch react application mainly on port 3000
- with showing all Udactiy courses only if the
attribute “available” = true and “open_for_enrollment” = true.
- Each course will have an enrollment button.

### Folder Structure

- `api/views/` - As Like Controller Holds files that define your endpoints
- `api/models/` - Holds files that defines your database schema
- `api/__init__.py` - What is initially ran when you start your application
- `api/utils.py` - utility functions and classes -
- `api/core.py` - includes core functionality including error handlers and logger
- `tests/` - Folder holding tests

--------------
- `frontEnd` - React project 
- `frontEnd/src/components` - List and ListCourse Component

#### Others

- `config.py` - Provides Configuration for the application. There are two configurations: one for development and one for production.
- `manage.py` - Command line interface that allows you to perform common functions with a command
- `requirements.txt` - A list of python package dependencies the application requires
- `Dockerfile` - instructions for Docker to build the Flask app
- `docker-compose.yml` - config to setup this Flask app and a Database
- `migrations/` - Holds migration files – doesn't exist until you `python manage.py db init` if you decide to not use docker
--------------


>By Abdolrhman Soliman 4 Udacity Assessment