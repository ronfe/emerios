__author__ = 'ronfe'

from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
import datetime
import threading
import calendar

db = MongoClient('10.8.8.111:27017')['yangcong-prod25']
events = db['mockEvents']
mock_events = db['mockEvents']
users = db['users']
user_attr = db['userAttr']

device_cache = db['deviceCache']

START_DATE = datetime.datetime(2015,11,1)
END_DATE = datetime.datetime(2015,11,3)

START_TIMESTAMP = calendar.timegm(START_DATE.utctimetuple())
END_TIMESTAMP = calendar.timegm(END_DATE.utctimetuple())