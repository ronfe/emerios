__author__ = 'ronfe'
import sys
sys.path.append('..')

from wheels import uf

new_users = uf.get_new_user_id()
user_count = len(new_users['devices'])

for k, v in new_users.iteritems():
    user_count += len(v)

print user_count