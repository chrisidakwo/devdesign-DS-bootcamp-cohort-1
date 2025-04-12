# Relative path
filePath = 'Week 4 - Working with Files/files/example.txt'

with open(filePath, 'r') as file:
    # Preferred method of looping through the lines in a file
    for line in file:
        print(line)

    print('')

    file.seek(0)

    # Alternative/manual method of looping through the lines in a file
    content = file.read() 
    for line in content.split('\n'):
        print(line)
