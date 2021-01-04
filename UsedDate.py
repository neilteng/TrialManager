import datetime
import NewDate

import os.path
from os import path
def usedDate():
    date = None
    if(path.exists('resources/latestDate.txt')):
        with open('resources/latestDate.txt','r') as file:
            date = file.readline()
            if(len(date)==0):
                date = NewDate.newDate()
            elif  int(datetime.datetime.now().strftime('%Y%m%d')) - int(date) > 100:
                # TODO: large gap since last trail
                pass
    else:
        date = NewDate.newDate()

    return date

#testing
# print(usedDate())