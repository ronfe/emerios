__author__ = 'ronfe'

from metaConfig import *

def get_all_user_id():
    pipeLine = [
        {"$match": {"createdBy": {"$gte": START_DATE, "$lt": END_DATE}}},
        {"$group": {"_id": None, "users": {"$addToSet": "$user"}}}
    ]
    a = list(events.aggregate(pipeLine))[0]['users']
    return a