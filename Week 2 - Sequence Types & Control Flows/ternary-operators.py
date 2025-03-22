# Ternary Operators - short-hand for if/else statements

print('')

age = input('Enter your age: ')
age = int(age)

# if age < 18:
#     category = 'dependent'
# else:
#     category = 'adult'

category = 'dependent' if (age < 18) else 'adult'

print(category)
print('')
