import sys
sys.path.append("..")

from wheels import *
from wheels import dataset

eventKeylist = [
    "enterGuidePage",
    "clickExperience",
    "enterSignupPage",
    "clickSignupBtn",
    "startChapter",
    "enterTopic",
    {"$in": ["startMaster", "startLearning"]},
    {"$in": ["finishVideo", "problemSetSuccess"]},
    {"$in": ["completeLearning", "completeMaster"]},
    "startVideo",
    "startMaster",
    "finishVideo",
    "problemSetSuccess",
    "completeLearning",
    "completeMaster",
]

for eventKey in eventKeylist:
    print("eventKey: %s")%(eventKey)
    uv = dataset.aggregate(eventKey)
    print(len(uv['device']) + len(uv['user']))
    print("")
