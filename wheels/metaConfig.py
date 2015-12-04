__author__ = 'ronfe'

from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
import datetime
import threading

db = MongoClient('10.8.8.111:27017')['yangcong-prod25']
events = db['points']
mock_events = db['mockEvents']
users = db['users']

device_cache = db['deviceCache']

START_DATE = datetime.datetime(2015,11,1)
END_DATE = datetime.datetime(2015,11,1,1)