__author__ = 'ronfe'
import sys
sys.path.append('..')

from wheels import uf
from wheels.metaConfig import *
new_users = uf.get_new_user_id()

print("9. 进入学习视频或练习 UV startLearning startMaster:")

pipeLine = [
    {"$match": {"eventKey": {"$in": ["startMaster", "startLearning"]}, "eventTime": {"$gte": START_DATE, "$lt": END_DATE}, "platform": "app", "platform2": "iOS"}},
    {"$group": {"_id": None, "devices": {"$addToSet": "$device"}}}
]

device_list = list(events.aggregate(pipeLine))[0]['devices']

pipeLine = [
    {"$match": {"eventKey": {"$in": ["startMaster", "startLearning"]}, "eventTime": {"$gte": START_DATE, "$lt": END_DATE}, "platform": "app", "platform2": "iOS"}},
    {"$group": {"_id": None, "users": {"$addToSet": "$user"}}}
]

user_list = list(events.aggregate(pipeLine))[0]['users']

result_device = set.intersection(set(new_users['devices']), set(device_list))

new_user_list = []
for k, v in new_users.iteritems():
    new_user_list.extend(v)

result_user = set.intersection(set(new_user_list), set(user_list))

print len(result_device) + len(result_user)
