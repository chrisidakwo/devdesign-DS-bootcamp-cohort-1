filePath = 'Week 4 - Working with Files/files/data-collector.txt'

print('')

fullName = input("Enter your full name: ")
print('')

subject = input("Enter the subject name: ")
print('')

score = float(input('Enter your score: '))
print('')

# Add content to the end of an existing file
with open(filePath, 'a') as file:
    file.write(f'{fullName},{subject},{score}' + '\n')
