__author__ = 'ronfe'

from metaConfig import *

def get_all_user_id():
    pipeLine = [
        {"$match": {"eventTime": {"$gte": START_DATE, "$lt": END_DATE}}},
        {"$group": {"_id": "$device", "users": {"$addToSet": "$user"}}}
    ]
    userPipeLine = [
        {"$match": {"eventTime": {"$gte": START_DATE, "$lt": END_DATE}}},
        {"$group": {"_id": "$user", "devices": {"$addToSet": "$device"}}}
    ]
    device_list = list(events.aggregate(pipeLine))
    user_list = list(events.aggregate(userPipeLine))

    unit_devices = []
    unit_users = {}
    for each in user_list:
        unit_devices.append(each['devices'][0])

    for each in device_list:
        if len(each['users']) > 1:
            unit_users[each['_id']] = each['users']


    return {
        "unitDevice": unit_devices,
        "unitUser": unit_users
    }

