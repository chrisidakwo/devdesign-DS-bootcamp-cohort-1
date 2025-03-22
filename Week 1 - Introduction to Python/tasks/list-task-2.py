# Task 2: Fast Food Orders 🍔

# A fast-food restaurant takes customer orders and stores them in a tuple to ensure they remain unchanged once confirmed.

# Instructions:

# Create a tuple named order that contains the following items: ("Burger", "Fries", "Soda").
# The restaurant now offers a "Super Meal" combo, which includes an additional "Ice Cream". However, tuples are immutable!
# Convert the tuple into a list, add "Ice Cream", and convert it back into a tuple.
# Print the modified tuple to confirm the update.
# Retrieve and print the first and last items in the order using their index positions.

order = ("Burger", "Fries", "Soda")
order = list(order)

order.append("Ice Cream")

order = tuple(order)

firstItem = order[0]
lastItem = order[-1]

print("First Item: ", firstItem)
print("Last Item: ", lastItem)