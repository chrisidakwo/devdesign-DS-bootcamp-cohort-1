# Local Scope
# Global Scope

# Variable Scope
# Defines the region where we can access and/or modify a variable. A variable can have either local or global scope depending where it was defined.

# Global scope
message = "Hello and Welcome"

def addNumbers(a, b):
    # The sumNums variable has a local scope given that it is defined inside the function
    # The message variable has a global scope given that it is defined outside the function

    # Local variable
    sumNums = a + b

    # Printing message which is a global variable
    print(message)

    return sumNums

def greeting(name):
    # To be able to modify the global variable 'message', we need to identify it as global inside this function
    # If we don't do this, the function will create a new local variable with the same name
    # and will not modify the global variable
    # The global keyword tells Python that we are referring to the global variable 'message'
    # and not creating a new local variable
    global message

    # This will create a new local variable 'message' inside the function because we referenced in above with the global keyword
    message = "Hello"
    print(message, name)

print('')
print('*************** FUNCTION SCOPE ***************')

# When we call this function, it will print the global variable 'message' which is "Hello and Welcome"
# and return the sum of the two numbers
print(addNumbers(7, 12))

print('')

# When we call this function, it will print the global variable 'message' which is "Hello Matthew"
# because we modified the value of the global variable 'message' inside the function
greeting('Matthew')

print('')

# When we call this function, it will print the global variable 'message' which is now "Hello" and no longer "Hello and Welcome"
# and return the sum of the two numbers
# The value of the global variable 'message' has been modified by the greeting function
print(addNumbers(7, 12))

# The value of the global variable 'message' is now "Hello" and not "Hello and Welcome"
print(f'What is the value of message?', message)
