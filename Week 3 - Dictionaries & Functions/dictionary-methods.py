# clear() - Removes all the elements from the dictionary

car1 = dict(
    brand = 'Ford',
    model = 'Mustang',
    engineLitre = 5.0,
    transmission = 'manual',
)

print('')
print(car1)

car1.clear()
print('')
print(car1)

# copy() Returns a shallow copy of the dictionary
car2 = dict(
    brand = 'Toyota',
    model = 'Corolla',
    engineLitre = 2.4,
    transmission = 'automatic',
)

copiedCar = car2.copy()
copiedCar['transmission'] = 'manual'

print('')
print(car2)
print(copiedCar)
print('')

print("The Toyota Corolla is automatic", car2['transmission'] == 'automatic')

# get() Returns the value of the specified key
print(car2.get('brand')) # cars2['brand']

person = {
    'firstName': 'John',
    'lastName': 'Doe',
    'age': 50,
    'pets': { 'dog': 'Frieda', 'cat': 'Sox' },
    'kids': ['Joe', 'Martha', 'Sarah']
}

print('')
secondChild = person.get('kids')[1]
print("The 2nd child's name is", secondChild)

dogName = person.get('pets').get('dog')
print("The dog's name is", dogName)


# items() - Returns a list containing a tuple for each key value pair
print('')
print(car2)
print(car2.items())

# values() - Returns a list of all the values in the dictionary
print('')
values = list(car2.values())
print(values)

# keys() - Returns a list of all the keys in the dictionary
print('')
keys = list(car2.keys())
print(keys)

print('')
print(dict(zip(keys, values)))

# pop() - Removes the element with the specified key and returns the value
lastName = person.pop('lastName')
print('')
print('LAST NAME', lastName)
print('')
print(person)


# update()