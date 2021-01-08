def updateTrailNumber(trialNumber):
    with open('resources/lastTrialNumber.txt','w+') as file:
        file.write(str(trialNumber))
    return trialNumber
