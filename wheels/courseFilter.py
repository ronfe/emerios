__author__ = 'ronfe'
from metaConfig import *

def weeklyTopicsEnterTop10():
    pipeLine = [
        {"$match": {"eventKey": "enterTopicList", "createdBy": {"$gte": START_DATE, "$lt": END_DATE}}},
        {"$group": {"_id": "$topic", "count": {"$sum": 1}}},
        {"$sort": {"count": DESCENDING}}
    ]

    x = list(events.aggregate(pipeLine))[:10]
    return [each["_id"] for each in x]
