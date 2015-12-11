__author__ = 'ronfe'
from metaConfig import *


def weeklyTopicsEnterTop10():
    pipeLine = [
        {"$match": {"eventKey": "enterTopic", "eventTime": {"$gte": START_TIMESTAMP, "$lt": END_TIMESTAMP}}},
        {"$group": {"_id": "$eventValue.topicId", "count": {"$sum": 1}}},
        {"$sort": {"count": DESCENDING}}
    ]

    x = list(events.aggregate(pipeLine))[:10]
    return [each["_id"] for each in x]


def weeklyStartMasterTop10():
    pipeLine = [
        {"$match": {
            "eventKey": "startMaster",
            "createdBy": {
                "$gte": START_DATE,
                "$lt": END_DATE
            }
        }},
        {"$group": {
            "_id": "$eventValue.topic",
            "count": {"$sum": 1}
        }},
        {"sort": {
            "count": DESCENDING
        }}
    ]

    x = list(events.aggregate(pipeLine))[:10]
    return [each["_id"] for each in x]
