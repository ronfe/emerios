__author__ = 'ronfe'

from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

db = MongoClient('10.8.8.111:27017')['yangcong-prod25']
events = db['points']
users = db['users']

START_DATE = datetime.datetime(2015,11,1)
END_DATE = datetime.datetime(2015,11,1,1)