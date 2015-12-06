__author__ = 'ronfe'

import networkx as nx
import sys, random
import string, datetime
sys.path.append('..')
from wheels import dc
import numpy as np

mock_events = dc.dbs('mockEvents')

def send_point(data):
    mock_events.insert_one(data)

dg = nx.DiGraph()

#-1 for quit app
dg.add_node(-1)

# 0 push notification alert 0-1 for "YES"/0.4 0-2 for "Dont allow"/0.6
dg.add_nodes_from([0,1,2])
dg.add_weighted_edges_from([(0,1,0.4), (0,2,0.6)])

# 3 guide page 1-3/1.0 2-3/1.0
# point 3 = enterGuidePage
# 4 for "start now" 5 for "register/login"
# 3-4/0.8 3-5/0.15 3--1/0.05
# point 4 = clickExperience
# point 5 = clickUserLogBtn
dg.add_nodes_from([3,4,5])
dg.add_weighted_edges_from([(1,3,1.0), (2,3,1.0)])
dg.add_weighted_edges_from([(3,4,0.8), (3,5,0.15), (3, -1, 0.05)])


candidates = range(2000)

user_paths = {}

quit_transfer = [0.0, 0.0, 0.0, 0.5, 1.0, 1.0]
state_transfer = [
    [0.0, 0.4, 0.6, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.8, 0.15],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
]

for each in candidates:
    cur_step = 0
    result_list = []
    quit_flag = False
    while not quit_flag:

        quit_prob = quit_transfer[cur_step]
        prob_chance = random.random()
        result_list.append(cur_step)
        # Quit?
        if prob_chance <= quit_prob:
            quit_flag = True
            result_list.append(-1)
        else:
            # transfer to what state?

            unit_state_transfer = np.array(state_transfer[cur_step])
            unit_random_sample = np.array([random.random() for i in range(len(unit_state_transfer))])

            multiple_result = unit_state_transfer * unit_random_sample
            next_state = int(np.where(multiple_result == multiple_result.max())[0])

            # Transfer to it
            cur_step = next_state

    user_paths[each] = result_list


print user_paths[3]