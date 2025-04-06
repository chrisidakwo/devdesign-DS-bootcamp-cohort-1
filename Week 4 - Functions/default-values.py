# A function can be created with default values assigned to any of its arguments
# In the case where a default value exists, such argument must come last
def sum(y, x = 13):
    return x + y

# All arguments in a function can have default value
def multiple(x = 13, y = 9):
    return x * y

print('')

sumValue = sum(x = 19, y = 20)
print(sumValue)