# Create a while loop that asks for a password until it's at least 8 characters long

password = ''

print('')

while len(password) < 8:
    password = input('Enter your password: ')

    if (len(password) < 8):
        print('Password too short, try again!')
        print('')

print('Password accepted!')

print('')
