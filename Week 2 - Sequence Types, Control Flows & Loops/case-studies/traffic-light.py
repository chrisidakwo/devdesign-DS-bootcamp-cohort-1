# Imagine you're driving and you reach a traffic light.

# If the light is green, you go.
# If the light is yellow, you slow down.
# If the light is red, you stop.

print('\n')

permittedColors = ('red', 'green', 'yellow')
lightColor = input('Enter either red, green, or yellow: ')

# Validate that the user input matches the permitted list of colors
if lightColor in permittedColors:
    if lightColor == "green":
        print('Go')
    elif lightColor == 'yellow':
        print('Slow down')
    else:
        print('Stop')
else:
    print('Please enter a valid color!')
