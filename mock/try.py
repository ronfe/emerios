__author__ = 'ronfe'
import sys, random
import string, datetime
sys.path.append('..')
from wheels import dc
import calendar

mock_events = dc.dbs('mockEvents')
user_attr = dc.dbs('userAttr')
user_list = user_attr.distinct("userId")

def send_point(data):
    mock_events.insert_one(data)


def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def randomuser(times):
    global user_list
    # user_list = users.distinct("_id")
    return random.sample(user_list, times)

chains = ["enterGuidePage", "clickUserLogBtn"]

ceiling = 1000
random_chains = [1000]
for i in range(1):
    a = random.randint(1, ceiling)
    ceiling = a
    random_chains.append(a)

print random_chains

devices = [randomword(10) for i in range(1000)]
users = randomuser(500)

template_event = {
    "eventKey": "",
    "category": "site",
    "eventTime": datetime.datetime(2015,11,1),
    "device": "",
    "platform": "app",
    "platform2": "iOS"
}

def random_longed(start_time):
    x = start_time + datetime.timedelta(seconds=random.randint(1, 60))
    x = calendar.timegm(x.utctimetuple())
    return x

for i in range(len(devices)):
    device_id = devices[i]
    curTime = template_event['eventTime']
    for event_index in range(len(chains)):
        if i < random_chains[event_index]:
            this_event = dict(template_event)
            this_event['eventKey'] = chains[event_index]
            this_event['eventTime'] = random_longed(curTime)
            curTime = datetime.datetime.fromtimestamp(this_event['eventTime'])
            this_event['device'] = device_id
            if i % 2 == 0:
                this_event['user'] = users[i / 2]
            mock_events.insert_one(this_event)

print 'done'