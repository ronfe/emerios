__author__ = 'ronfe'

from pymongo import MongoClient

db = MongoClient('mongodb://localhost:27017')['ronfe-simulation']
state = db['state']


def insert_state(state_index, description, next_state, point, user_prop):
    schema = {
        "stateIndex": state_index,
        "description": description,
        "next": next_state
    }

    if len(point.keys()) != 0:
        schema['point'] = point

    if user_prop != False:
        schema['userProp'] = user_prop
    state.insert_one(schema)



state_index = 8001
desc = "user choose grade 7A"
next_list = [
    {
        "8001": 0.16,
        "8002": 0.16,
        "8003": 0.16,
        "8004": 0.16,
        "8005": 0.16,
        "8006": 0.16,
        "-1": 0.04
    }
]

point = {
    # "eventKey": "clickUserLogBtn"
}

user_prop = False

insert_state(state_index, desc, next_list, point, user_prop)
