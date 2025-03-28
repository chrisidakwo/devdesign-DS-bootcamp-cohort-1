car = dict(
    brand = 'Ford',
    model = 'Mustang',
    engineLitre = 5.0,
    transmission = 'manual',
)

# You access values in a dictionary using a square bracket and the name of the key
print(car['transmission'])

person = {
    'firstName': 'John',
    'lastName': 'Doe',
    'age': 50,
    'pets': { 'dog': 'Frieda', 'cat': 'Sox' },
    'kids': ['Joe', 'Martha', 'Sarah']
}

print('')
print('What\'s the name of the 2nd child?')
secondChild = person['kids'][1] # person.get('kids')[1]
dogName = person['pets']['dog'] # person.get('pets').get('dog')

print('')
print('Name of the 2nd child is:', secondChild)

print('')
print('What\'s the name of his dog?')

print('')
print('Name of the dog is:', dogName)

