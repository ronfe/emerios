import sys

sys.path.append("..")

from wheels.metaConfig import *
from bson.objectid import ObjectId


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

        return topic_videos

    result = [converter(each) for each in topic_list]
    return result


topic_id = [ObjectId("54c708798bac81fccbd4bae5")]
print topic2video(topic_id)
