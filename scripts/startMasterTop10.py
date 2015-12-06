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

def completionRate(mEvent, dEvent, top10MasterList):
    m = dataset.aggregateTopic(mEvent, top10TopicsList)
    mNum = len(m['user']) + len(m['device'])
    d = dataset.aggregateTopic(dEvent, top10TopicsList)
    dNum = len(d['user']) + len(d['device'])
    return mNum/dNum

print("学习模块总完成率：")
print(completionRate("completeLearning", "startLearning", top10TopicsList))

# 视频总观看量
def startCompleteMaster(condition, top10TopicsList):
    user = dataset.aggregateTopic(condition, top10TopicsList)
    return len(user['device']) + len(user['user'])

print("视频总观看量：")
print(startFinishVideo("startVideo", top10TopicsList))
# 视频完成总量
print("视频完成总量：")
print(startFinishVideo("finishVideo", top10TopicsList))


# 练习进入总量
# 练习模块真实总完成率
# 完成量/真正进入量
# 挑战失败量/挑战进入量
# 挑战成功+失败量/挑战进入量
