import sys
from wheels.metaConfig import *
from bson.objectid import ObjectId

sys.path.append("..")


# Given a list of topic ID, returns a nested list of videoId
def topic2video(topic_list):
    def converter(unit_topic_id):
        topic_videos = []
        unit_topic = topics.find_one({"_id": unit_topic_id})
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


topic_id = [ObjectId("54c708798bac81fccbd4bb3c")]
print topic2problem(topic_id)
