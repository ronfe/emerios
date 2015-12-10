import sys
sys.path.append("..")

from wheels.metaConfig import *

def topic2video(topic_list):
    result = []
    def converter(topic_id):
        unit_topic = topics.finc_one({"_id": topic_id})
        unit_hypervideo = unit_topic