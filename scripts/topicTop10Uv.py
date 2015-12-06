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

# 学习模块总完成率
# 总完成量/总进入量

def completionRate(mEvent, dEvent, top10TopicsList):
    m = dataset.aggregateTopic(mEvent, top10TopicsList)
    mNum = len(m['user']) + len(m['device'])
    d = dataset.aggregateTopic(dEvent, top10TopicsList)
    dNum = len(d['user']) + len(d['device'])
    return mNum/dNum

print("学习模块总完成率：")
print(completionRate("completeLearning", "startLearning", top10TopicsList))

# 视频总观看量
def startFinishVideo(condition, top10TopicsList):
    user = dataset.aggregateTopic(condition, top10TopicsList)
    return len(user['device']) + len(user['user'])

print("视频总观看量：")
print(startFinishVideo("startVideo", top10TopicsList))
# 视频完成总量
print("视频完成总量：")
print(startFinishVideo("finishVideo", top10TopicsList))
