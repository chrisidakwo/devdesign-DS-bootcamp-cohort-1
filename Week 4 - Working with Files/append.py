import datetime

filePath = 'Week 4 - Working with Files/files/log.txt'

# Add content to the end of an existing file
with open(filePath, 'a') as file:
    file.write("New entry: " + str(datetime.datetime.now()) + "\n")
