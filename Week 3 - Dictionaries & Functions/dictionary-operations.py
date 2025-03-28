# Type checking
car = dict(
    brand = 'Ford',
    model = 'Mustang',
    engineLitre = 5.0,
    transmission = 'manual',
)

print('')

# Check data type
print('Check data type', type(car))

# Assert dictionary length
print('Assert the the dictionary length', len(car))
print('')

# To delete, use the key name of the value
del car['transmission']
print('Updated car', car)

print('Assert the the dictionary length', len(car))

# Access dictionary item
print(car['brand'])

# Update (or assign a new) dictionary item/entry
car['engineLitre'] = 5.1

print('')
print('Update Car', car)