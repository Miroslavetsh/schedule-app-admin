# Schedule App Admin

This is the second part of already existing schedule-app-ui, which main task of that is in comfortable schedule manipulating. Make changing of schedule for teacher more flexible, comfortable and very simple...

## How to run application

- Firstly, you need to install `python3`, `docker` and setup a local redis database with RedisJSON. To do the last one, you should run the command `docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest` [from official GitHub repo](https://github.com/RedisJSON/RedisJSON)

- Second step is to go throw your project folder directly to the root and run _app.py_ using `python3 app.py`

## Overview

Let me start from the _app.py_ file, there we have all our routes, also startup the Flask application. In the templates folder templates have been prepared for each route. Routes placed in the appropriate folder. About routes:

- `/` - the root or index.html file. Teachers can find themselves here and go throw to the _pairs_ page
- `/pairs` - the result after picking a teacher from select on index page.
- `/groups `- all of the groups place here.
- `/groups/add `- add a new group.
- `/groups/:id/update `- updating a certain group.
- `/groups/:id/delete `- delete a certain group.

### Local updates

create any folder and run to it
#cd /d D:\cod\folder
create virtual environment
#python3 -m venv name
run venv
#redis_sandbox\Scripts\activate
run app
#python app.py
also run image
