__author__ = 'ronfe'

from metaConfig import *

# user_ids = users.distinct("_id", filter={"activateDate": {"$exists": True}})
user_ids = user_attr.distinct("userId", filter={"activatedTime": {"$exists": True}})
result_device = {}


def process_cursor(cursor):
    for doc in cursor:
        device_id = str(doc['device'])
        if doc['platform2'] == 'iOS':
            event_time = datetime.datetime.fromtimestamp(doc['eventTime'] / 1000) - datetime.timedelta(hours=8)
        else:
            event_time = doc['serverTime']
        # user_id = doc['user']
        previous_device = device_cache.find_one({"deviceId": device_id})
        if previous_device == None:
            activate_date = event_time
        else:
            activate_date = min(event_time, previous_device['activateDate'])

        device_cache.find_one_and_replace({"deviceId": device_id}, {
            "deviceId": device_id,
            "activateDate": activate_date
        }, upsert=True)


cursors = events.parallel_scan(10)
# cursors = mock_events.parallel_scan(10)
threads = [
    threading.Thread(target=process_cursor, args=(cursor,)) for cursor in cursors
    ]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
