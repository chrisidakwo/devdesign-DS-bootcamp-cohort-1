# Integers/floats to strings
year = 2025
print(type(year))

year = str(2025)
print(type(year))

print("The current year is " + year)

print("The circumference of a circle is " + str(3.14))

# Strings to integers/floats

totalItems = "35"
unitPrice = 15000

totalCost = int(totalItems) * unitPrice
print(totalCost)
print(f"N{totalCost:.2f}")
