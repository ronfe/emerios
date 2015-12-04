__author__ = 'centsent'
from metaConfig import *

def aggregate(condition):
    pipeLine = [
        {
            "$match": {
                "eventKey": condition,
                "eventTime": {"$gte": START_DATE, "$lt": END_DATE},
                "platform": "app",
                "platform2": "iOS"
            }
        },
        {
            "$group": {
                "_id": None,
                "devices": {"$addToSet": "$device"}
            }
        }
    ]

    device_list = list(events.aggregate(pipeLine))[0]['devices']

    pipeLine = [
        {
            "$match": {
                "eventKey": condition,
                "eventTime": {"$gte": START_DATE, "$lt": END_DATE},
                "platform": "app",
                "platform2": "iOS"
            }
        },
        {"$group": {"_id": None, "users": {"$addToSet": "$user"}}}
    ]

    user_list = list(events.aggregate(pipeLine))[0]['users']

    result_device = set.intersection(set(new_users['devices']), set(device_list))

    new_user_list = []
    for k, v in new_users.iteritems():
        new_user_list.extend(v)

    result_user = set.intersection(set(new_user_list), set(user_list))

    return {
        device: result_device,
        user: result_user
    }

# dataset.aggregate("enterGuidePage")
# dataset.aggregate({$in: ["A", "B"]})

eventKeylist = [
    "enterGuidePage",
    "clickExperience",
    "enterSignupPage",
    "clickSignupBtn",
    "startChapter",
    "enterTopic",
    {"$in": ["startMaster", "startLearning"]},
    {"$in": ["finishVideo", "problemSetSuccess"]},
    {"$in": ["completeLearning", "completeMaster"]},
    "startVideo",
    "startMaster",
    "finishVideo",
    "problemSetSuccess",
    "completeLearning",
    "completeMaster",
]

for eventKey in eventKeylist:
    print("eventKey: %s")%(eventKey)
    dataset.aggregate(eventKey)
    print("")
