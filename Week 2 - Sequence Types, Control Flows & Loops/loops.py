message = "Welcome, Chris! Thanks for joining the session today!"
message = "Welcome, Adrian! Thanks for joining the session today!"
message = "Welcome, Boaz! Thanks for joining the session today!"
message = "Welcome, Segin! Thanks for joining the session today!"
message = "Welcome, David! Thanks for joining the session today!"

students = ["Chris", "Adrian", "Boaz", "Segun", "David", "Donald", "Bassey", "Biodun", "Chukwuezi", "Ifeoluwa"]
print('')

# Loop through each student name and print a welcome message for each student
for name in students:
    name = name.upper()
    print(f"Hello, {name}! See you tomorrow!")

print('')

# print("Modulus", 20 % 2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
evenNumbers = []

for num in range(1, 21):
    # Even numbers are numbers divisible by 2 - without a remainder
    if num % 2 == 0: # % (Modulus) returns the remainder of a division operation
        evenNumbers.append(num)

print("The even numbers are: ")
print(evenNumbers)

print('')

# The range() utility function generates a list of numbers wth a defined stop, or a combination of start and stop values
print("Result from range:")
for num in range(1, 11):
    print(num * 3 / 7)

print('')
