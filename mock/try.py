__author__ = 'ronfe'
import sys, random
import string, datetime
sys.path.append('..')
from wheels import dc

mock_events = dc.dbs('mockEvents')

def send_point(data):
    mock_events.insert_one(data)


def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

chains = ["enterGuidePage", "enterSignupPage", "switchLogin", "clickLoginBtn", "loginFailure"]

ceiling = 2000
random_chains = [2000]
for i in range(4):
    a = random.randint(1, ceiling)
    ceiling = a
    random_chains.append(a)

print random_chains

devices = [randomword(10) for i in range(2000)]

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
    return x

for i in range(len(devices)):
    device_id = devices[i]
    curTime = template_event['eventTime']
    for event_index in range(5):
        if i < random_chains[event_index]:
            this_event = dict(template_event)
            this_event['eventKey'] = chains[event_index]
            this_event['eventTime'] = random_longed(curTime)
            curTime = this_event['eventTime']
            this_event['device'] = device_id
            mock_events.insert_one(this_event)

print 'done'