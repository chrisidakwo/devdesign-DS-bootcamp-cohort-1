import random

filePath = 'Week 4 - Working with Files/files/random-names.txt'

def generateRandomName():
    firstNames = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Chris", "David"]
    lastNames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Emmmanuel", "Irinyemi"]

    return random.choice(firstNames) + ' ' + random.choice(lastNames)

# Add content to the end of an existing file
with open(filePath, 'a') as file:
    name = generateRandomName()
    file.write(name + '\n')