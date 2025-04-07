# Current working directory/folder (primary folder)
# Relative
# TODO: Leave a note on current working directory

# Opening and Closing Files

file = open('Week 4 - Working with Files/files/example.txt', 'r') # Pass in the file path. Opens in a read mode
content = file.read()
file.close()

print('')
print('USING TRADITIONAL METHOD')
print("************ CONTENT OF TEXT FILE ************")
print(content)

# Better way using context manager
# with open('Week 4 - Working with Files/files/example.txt', 'r') as file:
#     content = file.read()
#     print('')
#     print('USING CONTEXT MANAGER')
#     print("************ CONTENT OF TEXT FILE ************")
#     print(content)
