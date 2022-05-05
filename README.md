# Schedule App Admin
This is the second part of already existing schedule-app-ui, which main task of that is in comfortable schedule manipulating. Make changing of schedule for teacher more flexible, comfortable and very simple...


## How to run application

- Firstly, you need to install `python3`, `docker` and setup a local redis database with RedisJSON. To do the last one, you should run the command `docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest` [from official GitHub repo](https://github.com/RedisJSON/RedisJSON)

- Second step is to go throw your project folder directly to the root and run _app.py_ using `python3 app.py`

## Overview

Let me start from the _app.py_ file