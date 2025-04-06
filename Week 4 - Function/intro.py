# How to define a function
def greeting():
    print('Hello World!')

# Call a function to perform the operation(s) within said function
greeting()

# A function can take in parameters
print('')
def greetingWithName(xyz):
    print(f'Hello {xyz}!')

# When calling the function, you pass in arguments that match the position of the parameters
greetingWithName('Bankole')

print('')

# A function can take in more than one parameter
def sum(num1, num2):
    print(f'The sum of {num1} and {num2} is', num1 +  num2)

# When calling the function, you pass in arguments that match the position of the parameters
sum(9, 14)

print(' ')

# A function can return a value - meaning it can output a result/value
def sum(num1, num2):
    return num1 + num2

# When calling a function that returns a result/value, you can assign the result/value to a variable
# This is useful for reusing the result/value of the function in other parts of your code
# For example, let's say you want to calculate the sum of two numbers and store it in a variable
# You can do that like this:
sumOfNumbers = sum(5, 6)

print("The sum of 5 and 6 is", sumOfNumbers)

print('')

# Keyword and Positional Arguments

def studentRecord(name, score, grade):
    print(f'{name} scored {score} out of 100, and has a grade of {grade}')

studentRecord('Maria', grade = 'C', score = 78.5)

# When using a mix of keyword and positional arguments, the positional arguments must come first.
# And you must provide the first positional argument before the keyword arguments
# The order of keyword arguments does not matter
studentRecord('Jeffrey', grade = 'A', score = 82)

# You can also use keyword arguments to specify the order of the parameters
# This allows you to pass in the arguments in any order
# For example, you can call the function like this:
studentRecord('Maria', score = 78.5)

# You can also use keyword arguments to specify the order of the parameters
# This allows you to pass in the arguments in any order
# For example, you can call the function like this:
studentRecord(score = 90, name = 'Jeffrey')

print('')
