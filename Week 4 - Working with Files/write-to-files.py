filePath = 'Week 4 - Working with Files/files/greeting.txt'

with open(filePath, 'w') as file:
    file.write("Hello, Marvellous!\n")
    file.write("This is a new line!")

# Write multiple lines at once
namesFilePath = 'Week 4 - Working with Files/files/names.txt'

names = ["Chris Idakwo", "David Irinyemi", "Emmanuel Ezugwu", "Fola Onipede", "Hannah Odumosu"]

# TODO: Do not add line break after the last name on the list

with open(namesFilePath, 'w') as file:
    # WRITE EACH NAME ON A NEW LINE

    # for name in names:
    #     file.write(name + '\n')

    # Using list comprehension
    newNames = [name + '\n' for name in names]
    file.writelines(newNames)