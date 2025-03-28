# A dictionary is a (an ordered) collection of key-value pairs

# METHOD 1: Using dictionary literal
profile = {
    'name': 'Chris Idakwo',
    'age': 20,
    'employed': True,
    'height': 1.68,
}

car1 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'engineLitre': 5.0,
    'transmission': 'manual',
}

print('')
print(car1)

# METHOD 2.1: The dictionary constructor
car2 = dict(
    brand = 'Ford',
    model = 'Mustang',
    engineLitre = 5.0,
    transmission = 'manual',
)

print('')
print(car2)

# METHOD 2.2: From sequence of values
countriesAndCapitals1 = dict([
    ('Nigeria', 'Abuja'),
    ('Ghana', 'Accra'),
    ('Kenya', 'Nairobi'),
    ('Malawi', 'Lilongwe'),
    ('England', 'London'),
])

print('')
print('2.2', countriesAndCapitals1)

# METHOD 2.3: From sequence of values

countries = [
    "Nigeria", "Ghana", "Kenya", "Malawi", "England"
]

capitals = [
    "Abuja", "Accra", "Nairobi", "Lilongwe", "London"
]

print('')

countriesAndCapitals2 = dict(zip(countries, capitals))
print("COUNTRIES AND CAPITALS", countriesAndCapitals2)

print('')
