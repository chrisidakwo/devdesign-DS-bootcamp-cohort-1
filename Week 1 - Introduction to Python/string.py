# string
name = "Chris Idakwo"

# integer
age = 20

# float (Floating-point number)
pi = 3.14 

# boolean
print(True)
print(False)

state = "Rivers"

# type() provides you information on the data type of a value
print(type(state))

# Finding the length of a string - the number of characters
print("Chris")

location = "Abuja"
print(len(location))

eventName = "UEFA Champions League"

# lower() transforms all letters in a text to lower case
print(eventName.lower())

# capitalize() transforms the first letter in a text to upper case 
print(eventName.capitalize())

# upper() transforms all the letters in a text to upper case
print(eventName.upper())

# title() transforms the first letter and every subsequent letter after a space to upper case
print(eventName.title())

print("2025".isnumeric())

print("-/chris.idakwo@gmail.com&-".strip("-&/"))


firstName = "John"
lastName = "Doe"
score = 80

# Concatenation - merge two or more strings
print(firstName + " " + lastName + " scored " + str(score) + " out of 100")

# f-string: Used for formatting strings
# You can insert valid Python code within the curly braces
print(f"{firstName.upper()} {lastName} scored {score} out of 100")

# Format
print("My name is {fname}. I'm {age} years old".format(fname = "Chris", age = 30))

# Operations within strings
print(f"The average of 80, 90, 120, and 40 is: {(80 + 90 + 120 + 40) / 4}")

# Format decimals within a string
print(f"The total price for your purchase is: {25000:.2f}")
print(f"The circumference of a circle is: {3.1415926535:.4f}")

# Escape Characters
print('The boy\'s parents were in school today')
print('This should insert \\ a single backlash')
print('Chris 80\nJoe 85\nMark 90')

print('First Name\tLast Name\tScore')
print("Chris\t\tIdakwo\t\t80")
print("Joe\t\tMatthew\t\t85")

# Create 2 variables to hold your first name and last name. Merge both string variables into a new variable. Print the new variable to the terminal.
firstName = "Danny"
lastName = "Hassan"

# Using f-string
# fullName = f"{firstName} {lastName}"

# Using concatenation
fullName = firstName + " " + lastName

print(fullName)

names = "Chris,Mike,Jane,Blessing,Peter,Joe,Sarah,Daniel"
print(names)
print(names.split(","))
