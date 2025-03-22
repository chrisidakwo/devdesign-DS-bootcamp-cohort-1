emailAddress = input("Enter your email address: ")
password = input("Enter your password: ")
print(emailAddress)
print(password)

# strip() trims whitespace (or any other defined character) on either ends of a string
print(emailAddress.strip("-"))

# replace() is used to replace a character in a string
print(emailAddress.replace("-", "_"))
print(emailAddress.replace("-", ""))

print(emailAddress.endswith("f"))

question1 = input("What is the result of 5 x 7?")
print("\n\nThe result is: " + question1)