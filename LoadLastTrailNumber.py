import os.path
from os import path

def lastTrailNumber():
    trialNumber = None
    if(path.exists('resources/lastTrialNumber.txt')):
        with open('resources/lastTrialNumber.txt','r') as file: 
            trialNumber = file.readline()
            if len(trialNumber) == 0:
                with open('resources/lastTrialNumber.txt','w+') as file: 
                    trialNumber = 1
                    file.write(str(trialNumber))
            elif int(trialNumber) < 0:
                # TODO: exception for trial number < 0
                pass
    else:
         with open('resources/lastTrialNumber.txt','w+') as file: 
            trialNumber = 1
            file.write(str(trialNumber))
            
    return trialNumber
