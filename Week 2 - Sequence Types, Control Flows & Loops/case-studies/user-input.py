# "Let's create a program that asks for user input until they type 'quit'"

print('')

userInput = ''
responses = []

while userInput != 'quit':
    userInput = input("Enter some text (or 'quit' to exit): ")

    if userInput != 'quit':
        responses.append(userInput)

print('You entered the following texts:', responses)
