person = {}

person['firstName'] = 'Daniel'
person['lastName'] = 'Doe'
person['age'] = 35
person['dob'] = "16/03/1980"

# Use the update() method to 'update' and/or add new entry to a dictionary
person.update({ 'nationality': 'Ghanian' })

print('')
print(person)

print('')
car = dict(
    brand = 'Ford',
    model = 'Mustang',
    engineLitre = 5.0,
    transmission = 'manual',
)

car['transmission'] = 'automatic'
car['engineLitre'] = 4.8
car['engineType'] = 'v8'

print(car)
