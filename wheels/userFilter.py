__author__ = 'ronfe'

from metaConfig import *

# API used for testing
def test():
    return "I am testing"

def get_all_user_id():
    pipeLine = [
        {"$match": {"eventTime": {"$gte": START_TIMESTAMP, "$lt": END_TIMESTAMP}}},
        {"$group": {"_id": "$device", "users": {"$addToSet": "$user"}}}
    ]
    userPipeLine = [
        {"$match": {"eventTime": {"$gte": START_TIMESTAMP, "$lt": END_TIMESTAMP}}},
        {"$group": {"_id": "$user", "devices": {"$addToSet": "$device"}}}
    ]
    # device_list = list(events.aggregate(pipeLine))
    # user_list = list(events.aggregate(userPipeLine))
    device_list = list(mock_events.aggregate(pipeLine))
    user_list = list(mock_events.aggregate(userPipeLine))

    unit_devices = []
    unit_users = {}
    for each in user_list:
        unit_devices.append(each['devices'][0])

    for each in device_list:
        if len(each['users']) > 1:
            unit_users[str(each['_id'])] = each['users']
        elif len(each['users']) == 0:
            unit_devices.append(each['_id'])

    return {
        "devices": list(set(unit_devices)),
        "users": unit_users
    }

def get_new_user_id():
    all_users = get_all_user_id()
    # New devices
    result = {
        "devices": [],
        "users": {}
    }

    def judge_device(device_id):
        x = device_cache.find_one({"deviceId": device_id, "activateDate": {"$gte": START_DATE, "$lt": END_DATE}})
        if x == None:
            return False
        else:
            return True

    def judge_user(user_id):
        # x = users.find_one({"_id": user_id, "activateDate": {"$gte": START_DATE, "$lt": END_DATE}})
        x = user_attr.find_one({"userId": user_id, "activatedTime": {"$gte": START_DATE, "$lt": END_DATE}})
        if x == None:
            return False
        else:
            return True


    result["devices"] = [each for each in all_users["devices"] if judge_device(each)]
    for k, v in result["users"].iteritems():
        user_list = v
        temp = [each for each in user_list if judge_user(each)]
        if len(temp) == 0:
            result["users"].pop(k)
        elif len(temp) == 1:
            device_id = ObjectId(k)
            result["devices"].append(device_id)
        else:
            result["users"][k] = temp

    return result
