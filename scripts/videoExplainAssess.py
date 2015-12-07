# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

# 周前十知识点学习模块

from wheels import *
from wheels import dataset
from wheels import courseFilter
from wheels import userFilter

top10Topics = courseFilter.weeklyTopicsEnterTop10()
top10TopicsList = []
for i in range(10):
    top10TopicsList.append(str(top10Topics[i]))

def clickAssess(top10TopicsList):
    pipeLine = [
        {"$match": {
            "eventKey": clickExpVideo,
            "eventValue.topicId": {"$in": top10TopicsList}
        }},
        {"$group": {
            "_id": None,
            "users": {"$addToSet": top10TopicsList}
        }}
    ]
    return list(events.aggregate(pipeLine))

print(len(clickAssess(top10TopicsList)))

def clickAssessWhenFalse(top10TopicsList):
    pipeLine = [
        {"$match": {
            "eventKey": clickExpVideo,
            "eventValue.problemState": "incorrect"
        }},
        {"$group": {
            "_id": None,
            "users": {"$addToSet": top10TopicsList}
        }}
    ]
    return list(events.aggregate(pipeLine))
    
print(len(clickAssessWhenFalse(top10TopicsList)))
