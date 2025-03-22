# Comparison Operators: ==, !=, >, <, >=, <=

# == "Equal to"
# The double "equal to" sign is used to compare two values. If the values are equal, the result is True. If the values are not equal, the result is False.

isEqual1 = 10 == 2 # False
isEqual2 = 2 == 2 # True
isEqual3 = "Hello" == "hello" # False

# print(isEqual1)
# print(isEqual2)
# print(isEqual3)

# != "Not equal to"
notEqual1 = 10 != 2 # True
notEqual2 = 2 != 2 # False
notEqual3 = "Hello" != "hello" # True

print(f"Not Equal 1: {notEqual1}")
print(f"Not Equal 2: {notEqual2}")
print(f"Not Equal 3: {notEqual3}")

print("\n\n")

# > "Greater than"
gt1 = 28 > 5 # True
gt2 = 10 > 23 # False
print(f"Greater than 1: {gt1}")
print(f"Greater than 2: {gt2}")

print("\n")

# < "Less than"
lt1 = 28 < 5 # False
lt2 = 10 < 23 # True
print(f"Less than 1: {lt1}")
print(f"Less than 2: {lt2}")

print("\n")

# Greater than OR equal to
gte1 = 45 >= 45 # True
gte2 = 74 >= 24 # True
gte3 = 74 >= 86 # False
print(f"gte1: {gte1}")
print(f"gte2: {gte2}")
print(f"gte3: {gte3}")

# Less than OR equal to
lte1 = 45 <= 45 # True
lte2 = 74 <= 24 # False
lte3 = 74 <= 86 # True
print(f"lte1: {lte1}")
print(f"lte2: {lte2}")
print(f"lte3: {lte3}")
