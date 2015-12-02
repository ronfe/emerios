# _*_ coding: utf8 _*_

# TODO: 新用户如何鉴定
# 获取新用户后各个事件的event

from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# link to db
dbClient = MongoClient('mongodb://10.8.8.111:27017')
db = dbClient['miner-prod25']

# open collections
points = db['points']
users = db['users']

# configure daterange
startDate = datetime.datetime(2015,11,15)
endDate   = startDate + datetime.timedelta(days = 2)

def eventUvCount(startDate, endDate, event):
    pipeLine = [
        {"$match": {
            "eventKey": event
        }},
        {"$group": {
            "_id": {"$addToSet": "$_id"}
        }}
    ]
    return list()

print("######新用户当天行为######")
print("新用户")
# TODO: wait ronfe

print("进入启动页面 UV")
enterStartPage =
print(len(enterStartPage))

print("启动页点击“免费使用”UV")
clickFreeToUse =
print(len(clickFreeToUse))

print("进入注册页 UV")
enterRegPage =
print(len(enterRegPage))

print("在注册页点击“注册” UV")
clickSignIn =
print(len(clickSignIn))

print("完成注册点击“进入我的学习” UV")
enterMyStudyProfile =
print(len(enterMyStudyProfile))

print("进入章节页 UV")
enterChapterPage =
print(len(enterChapterPage))

print("进入知识点 UV")
enterTopicList =
print(len(enterTopicList))

print("进入学习视频或练习 UV")
enterPlayVideoOrPractice =
print(len(enterPlayVideoOrPractice))

print("完成第一个学习视频或一个专题 UV")
finishFirstPlayVideoOrPractice =
print(len(finishFirstPlayVideoOrPractice))

print("完成学习模块或练习模块")
finishStudyModuleOrPracticeModule =
print(len(finishStudyModuleOrPracticeModule))

print("进入学习视频 UV")
enterPlayVideo =
print(len(enterPlayVideo))

print("进入练习UV")
enterPractice =
print(len(enterPractice))

print("完成一个学习视频 UV")
finishPlayVideo =
print(len(finishPlayVideo))

print("完成一个专题 UV")
finishProblemSet =
print(len(finishProblemSet))

print("完成学习模块 UV")
finishStudyModule =
print(len(finishStudyModule))

print("完成练习模块")
finishPracticeModule =
print(len(finishPracticeModule))

print("######新用户当天行为######")
