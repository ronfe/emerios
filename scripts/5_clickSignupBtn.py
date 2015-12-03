__author__ = 'ronfe'
import sys
sys.path.append('..')

from wheels import uf
from wheels.metaConfig import *
new_users = uf.get_new_user_id()

print("5. 在注册页点击“注册” UV clickSignupBtn:")

pipeLine = [
    {"$match": {"eventKey": "clickSignupBtn", "eventTime": {"$gte": START_DATE, "$lt": END_DATE}, "platform": "app", "platform2": "iOS"}},
    {"$group": {"_id": None, "devices": {"$addToSet": "$device"}}}
]

device_list = list(events.aggregate(pipeLine))[0]['devices']

pipeLine = [
    {"$match": {"eventKey": "clickSignupBtn", "eventTime": {"$gte": START_DATE, "$lt": END_DATE}, "platform": "app", "platform2": "iOS"}},
    {"$group": {"_id": None, "users": {"$addToSet": "$user"}}}
]

user_list = list(events.aggregate(pipeLine))[0]['users']

result_device = set.intersection(set(new_users['devices']), set(device_list))

new_user_list = []
for k, v in new_users.iteritems():
    new_user_list.extend(v)

result_user = set.intersection(set(new_user_list), set(user_list))

print len(result_device) + len(result_user)
