# Logical Operators - and, or, not

temperature = 35
humidity = 15

orCheck1 = temperature > 30 or humidity < 10 # True or False
andCheck1 = temperature > 30 and humidity < 20 # True and True

orCheck2 = temperature < 30 or humidity < 20 # False or True
andCheck2 = temperature < 30 and humidity < 10 # False and False

print(f"orCheck1: {orCheck1}")
print(f"andCheck1: {andCheck1}")

print("")

print(f"orCheck2: {orCheck2}")
print(f"andCheck2: {andCheck2}")

# Truth table

# OR Rules
# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

# And Rules
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False