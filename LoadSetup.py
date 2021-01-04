def loadSetup(filename):
    # print(filename)
    with open(filename,'r')  as file:
        # print(''.join(file.read().splitlines()) )
        return ''.join(file.read().splitlines()) 