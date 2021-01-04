def updateDir(dir = './'):
    with open('resources/workingDirectory.txt','w+') as file:
        file.write(dir)