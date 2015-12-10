__author__ = 'ronfe'

from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
import datetime
import threading
import calendar

db = MongoClient('10.8.8.111:27017')['onlinedb30']
another_db = MongoClient('10.8.8.111:27017')['yangcong-prod25']
db_3 = MongoClient('10.8.8.111:27017')['onions-cb']
events = db['events']
users = db['users']
user_attr = another_db['userAttr']
device_cache = db['deviceCache']
topics = db_3['topics']
hypervideos = db_3['hypervideos']

START_DATE = datetime.datetime(2015,11,1)
END_DATE = datetime.datetime(2015,11,1,1)

START_TIMESTAMP = calendar.timegm(START_DATE.utctimetuple())
END_TIMESTAMP = calendar.timegm(END_DATE.utctimetuple())
