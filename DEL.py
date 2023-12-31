"""
delte misskey notes posted a month ago
"""
from misskey import Misskey
import os
import datetime
import time

# get environment variables
token = os.environ['mktoken']
domain = os.environ['DOMAIN']

mk = Misskey(domain, i=token)

# get user id
my_id = mk.i()["id"]
print('my id: ' , my_id)
  


# print('status:')
# print(status)

# delete notes from the status dict

while True:
    status = mk.users_notes(user_id=my_id, until_date=datetime.datetime.now() - datetime.timedelta(days=120), limit=100)  
    if  status == []:
        print('no notes to delete')
        break
    time.sleep(12)
    
    for note in status:
        try:
            mk.notes_delete(note["id"])
            print('deleted: ', note["id"])
            time.sleep(12)
        except Exception as e:
            print(e)
            time.sleep(12)
            continue

    
    