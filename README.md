# Schedule App Admin

This is the second part of already existing schedule-app-ui, which main task of that is in comfortable schedule manipulating. Make changing of schedule for teacher more flexible, comfortable and very simple...

## How to run application

- Firstly, you need to install `python3`

- Second step is to go throw your project folder directly to the root and run _app.py_ using `python3 app.py` or `flask run` inside the root folder

## Overview

Let me start from the _app.py_ file, there we have all our routes, also startup the Flask application. In the templates folder templates have been prepared for each route. Routes placed in the appropriate folder. Each page also has a link to the homepage. Info about routes is in the next paragraph.

## Routes

#### pairs

- `/pairs` - GET all pairs
- `/pairs` - POST adding a new pair to the pairs table
- `/pairs/:id` - GET after filling the adding a new one pair
- `/pairs/:id` - PUT to update a pair from pairs list
- `/pairs/:id` - DELETE to remove a pair from pairs list

#### subjects

- `/subjects` - GET all subjects
- `/subjects` - POST adding a new subject to the subjects table
- `/subjects/:id` - GET after filling the adding a new one subject
- `/subjects/:id` - PUT to update a subject from subjects list
- `/subjects/:id` - DELETE to remove a subject from subjects list

#### teachers

- `/teachers` - GET all teachers
- `/teachers` - POST adding a new teacher to the teachers table
- `/teachers/:id` - GET after filling the adding a new one teacher
- `/teachers/:id` - PUT to update a teacher from teachers list
- `/teachers/:id` - DELETE to remove a teacher from teachers list

#### schedules

- `/schedules` - GET all schedules
- `/schedules` - POST adding a new schedule to the schedules table
- `/schedules/:id` - GET after filling the adding a new one schedule
- `/schedules/:id` - PUT to update a schedule from schedules list
- `/schedules/:id` - DELETE to remove a schedule from schedules list

#### groups

- `/groups` - GET all groups
- `/groups` - POST adding a new group to the groups table
- `/groups/:id` - GET after filling the adding a new one group
- `/groups/:id` - PUT to update a group from groups list
- `/groups/:id` - DELETE to remove a group from groups list

## How to run it locally

- Firstly, you need to get access to the Redis Cloud DB, which contains all of the entities, so we provide to you some credentials placed in `.env` file

- Secondly, run a _fill_redis.py_ file with `python helpers/fill_redis.py` command

- Thirdly, install all pip requirements and run `flask-run` from root of the project. Now you got your local setup of Flask application

## Deployment

### The root endpoint _/_ is UNAVAILABLE

[staging](http://schedule-app-admin.herokuapp.com/)
