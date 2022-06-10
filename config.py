import os
from flask import Flask
import logging
from dotenv import load_dotenv
from redis import Redis
from flask_cors import CORS

load_dotenv()
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = int(os.environ['REDIS_PORT'])
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

logging.basicConfig(filename="logfile.txt",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.debug("Logging test...")

app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

db = Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
