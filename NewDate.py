import datetime
def newDate():
    date = datetime.datetime.now().strftime('%Y%m%d')
    with open('resources/latestDate.txt', "w+") as file: 
        file.write(date)
    return date

# testing
# newDate()
# print(type(datetime.datetime.now().strftime('%Y%m%d')))