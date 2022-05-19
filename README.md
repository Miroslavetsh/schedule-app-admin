# Schedule App Admin

This is the second part of already existing schedule-app-ui, which main task of that is in comfortable schedule manipulating. Make changing of schedule for teacher more flexible, comfortable and very simple...

## How to run application

- Firstly, you need to install `python3`, `docker` and setup a local redis database with RedisJSON. To do the last one, you should run the command `docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest` [from official GitHub repo](https://github.com/RedisJSON/RedisJSON)

- Second step is to go throw your project folder directly to the root and run _app.py_ using `python3 app.py`

## Overview

Let me start from the _app.py_ file, there we have all our routes, also startup the Flask application. In the templates folder templates have been prepared for each route. Routes placed in the appropriate folder. Each page also has a link to the homepage. Info about routes is in the next paragraph.

## Routes

#### index

- `/` - the root or index.html file. Here we provided the teachers list(GET) for select and made form with approving current teacher to get his own pairs

#### pairs

- `/pairs` - GET pairs for current teacher after entering a teacher name
- `/pairs/add` - POST after filling the adding a new one pair
- `/pairs/<pair_id>/delete/` - DELETE|POST to remove a pair from pairs list and then back to index
- `/pairs/<pair_id>/update/` - PATCH|PUT|POST to update a pair from pairs list and then back to index

#### subjects

- `/subjects` - GET all subjects
- `/subjects/add` - POST after filling the adding a new one subject, and also giving all of the subjects
- `/subjects/<subject_id>/delete/` - DELETE|POST to remove a subject from subjects list and then back to index
- `/subjects/<subject_id>/update/` - PATCH|PUT|POST to update a subject from subjects list and then back to index

#### teachers

- `/teachers` - GET all teachers
- `/teachers/add` - POST after filling the adding a new one teacher
- `/teachers/<teacher_id>/delete/` - DELETE|POST to remove a teacher from teachers list and then back to index
- `/teachers/<teacher_id>/update/` - PATCH|PUT|POST to update a teacher from teachers list and then back to index

#### schedules

- `/schedules` - GET schedules for current schedule after entering a schedule name
- `/schedules/add` - POST after filling the adding a new one schedule
- `/schedules/<schedule_id>/delete/` - DELETE|POST to remove a schedule from schedules list and then back to index
- `/schedules/<schedule_id>/update/` - PATCH|PUT|POST to update a schedule from schedules list and then back to index

#### groups

- `/groups` - GET groups for current group after entering a group name
- `/groups/add` - POST after filling the adding a new one group
- `/groups/<group_id>/delete/` - DELETE|POST to remove a group from groups list and then back to index
- `/groups/<group_id>/update/` - PATCH|PUT|POST to update a group from groups list and then back to index

## How to run it locally

- Firstly, you need to install a docker with related `redis-redisjson` container and run it, next - open a CLI by clicking on a cli button and run `redis-cli` command

- Secondly, run a _fill_redis.py_ file with `python helpers/fill_redis.py` command

- Thirdly, install all pip requirements and run `flask-run` from root of the project. Now you got your local setup of Flask application
