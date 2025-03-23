# You want to create a simple task manager that helps you stay productive.

# Task:
# Create an empty list called tasks.
# Use a while loop to ask the user to enter tasks until they type "done".
# Print all the tasks they entered.
# If they entered "urgent" as a task, print: "You have urgent tasks to complete!"

print('')

tasks = []
taskInput = ''

while taskInput != 'done':
    taskInput = input('Enter a task (or \'done\' to exit): ')

    if taskInput == 'urgent':
        print('You have urgent tasks to complete!')
        print('')
    
    tasks.append(taskInput)
        

print('Here\'s a list of your tasks:', tasks)

print('')