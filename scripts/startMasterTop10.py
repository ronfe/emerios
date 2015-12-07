# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

# 周前十知识点学习模块

from wheels import *
from wheels import dataset
from wheels import courseFilter
from wheels import userFilter

top10Master = courseFilter.weeklyStartMasterTop10()
top10MasterList = []
for i in range(10):
    top10MasterList.append(str(top10Master[i]))

# 练习进入总量
def startMasterTotalNumber(top10MasterList):
    pipeLine = [
        {"$match": {
            "eventKey": "startMaster",
            "eventValue.topicId": top10MasterList
        }},
        {"$group": {
            "_id": None,
            "users": {"$addToSet": "$user"}
        }}
    ]

    return list(events.aggregateMaster(pipeLine))

# 挑战失败量/挑战进入量
def failureRetetion(top10MasterList):
    pipeLine = [
        {"$match": {
            "eventKey": "completeMaster",
            "eventValue.topicId": top10MasterList
        }},
        {"$group": {
            "_id": None,
            "users": {"$addToSet": "$user"}
        }}
    ]
    completeMasterNum = len(list(events.aggregateMaster(pipeLine)))

    pipeLine = [
        {"$match": {
            "eventKey": "startMaster",
            "eventValue.topicId": top10MasterList
        }},
        {"$group": {
            "_id": None,
            "users": {"$addToSet": "$user"}
        }}
    ]
    startMasterNum = len(list(events.aggregateMaster(pipeLine)))

    return completeMasterNum/startMasterNum


# 挑战完成率
# 挑战成功+失败量/挑战进入量
def successFinishRetetion(top10MasterList):
    pipeLine = [
        {"$match": {
            "eventKey": {"$in": ["challengeFailure", "challengeSuccess"]},
            "eventValue.topicId": {"$in": top10MasterList}
        }},
        {"$group": {
            "_id": None,
            "users": {"$addToSet": "$user"}
        }}
    ]
    successAndFailureNum = len(list(events.aggregateMaster(pipeLine)))

    pipeLine = [
        {"$match": {
            "eventKey": "startChallenge",
            "eventValue.topicId": {"$in": top10MasterList}
        }},
        {"$group": {
            "_id": None,
            "users": {"$addToSet": "$user"}
        }}
    ]
    finishNum = len(list(events.aggregateMaster(pipeLine)))

    return successAndFailureNum/finishNum

print("挑战完成率: %s")%(successFinishRetetion(top10MasterList))
