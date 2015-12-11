import sys
from wheels.metaConfig import *
import wheels.userFilter as uf
import wheels.courseFilter as cf
from bson.objectid import ObjectId

sys.path.append("..")


# Given a list of topic ID, returns a nested list of videoId
def topic2video(topic_list):
    def converter(unit_topic_id):
        topic_videos = []
        unit_topic = topics.find_one({"_id": ObjectId(unit_topic_id)})
        unit_hypervideo = unit_topic['learning']['hyperVideos']
        if len(unit_hypervideo) > 0:
            for each_hv in unit_hypervideo:
                unit_hv = hypervideos.find_one({"_id": each_hv})
                if "video" in unit_hv.keys():
                    topic_videos.append(unit_hv['video'])
        else:
            topic_videos.append([])

        return topic_videos

    result = [converter(each) for each in topic_list]
    return result


# Given a list of topic ID, returns a nested list of problemSet ids
def topic2problem(topic_list):
    def converter(unit_topic_id):
        topic_problemsets = []
        unit_topic = topics.find_one({"_id": unit_topic_id})
        unit_problemset = unit_topic['master']['problemSets']
        if len(unit_problemset) > 0:
            for each_ps in unit_problemset:
                topic_problemsets.append(each_ps)
        else:
            topic_problemsets.append([])

        return topic_problemsets

    result = [converter(each) for each in topic_list]
    return result


def calc_uv(candidate_match):
    # step 1: get all the active users
    active_users = uf.get_all_user_id()

    # round 1: get unique device
    pipeline = [
        {"$match": candidate_match},
        {"$match": {"device": {"$in": active_users['devices']}}},
        {"$group": {"_id": None, "devices": {"$addToSet": "$device"}}}
    ]
    # print list(events.aggregate(pipeline))
    round_1_num = list(events.aggregate(pipeline))
    if len(round_1_num) > 0:
        round_1_num = len(round_1_num[0]['devices'])
    else:
        round_1_num = 0

    # round 2: get unique users
    multiple_users = active_users['users'].values()

    pipeline = [
        {"$match": candidate_match},
        {"$match": {"user": {"$exists": True}}},
        {"$match": {"user": {"$in": multiple_users}}},
        {"$group": {"_id": None, "users": {"$addToSet": "$user"}}}
    ]
    round_2_num = list(events.aggregate(pipeline))
    if len(round_2_num) > 0:
        round_2_num = len(round_2_num[0]['users'])
    else:
        round_2_num = 0

    return round_1_num + round_2_num


# Get a nested list of videoIds and an eventkey returns a list of uvs
def get_video_times(video_list, event_key):
    event_match = {"eventKey": event_key, "eventValue.videoId": {"$in": [str(each) for each in video_list]}}
    return calc_uv(event_match)


# topic_id = [ObjectId("54c708798bac81fccbd4bb3c")]
topic_ids = cf.weeklyTopicsEnterTop10()
a = topic2video(topic_ids)
res = []
for each in a:
    res.append(get_video_times(each, 'startVideo'))
# res = get_video_times(a, "finishVideo")
print res
