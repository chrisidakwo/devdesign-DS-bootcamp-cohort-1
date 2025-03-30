# Pet shop inventory
petShop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}

print('')
print(petShop)

# 1. Add a new type of animal
petShop['animals']['birds'] = {
    'Parakeet': 4,
    'Canary': 3,
    'Cockatiel': 7,
}

# Using the update() method
# petShop['animals'].update({
#     'birds',
#     { 'Parakeet': 4, 'Canary': 3, 'Cockatiel': 7 }
# })

# 2. Update the quantity of a supply item after a sale
print('')
print(petShop['supplies']['habitats'])

catTrees = petShop['supplies']['habitats']['Cat Trees']

# For example, we sold 3 cat trees
petShop['supplies']['habitats']['Cat Trees'] = catTrees - 3

# TODO: Make this dynamic
# supplyCategory = input('Enter the supply category (habitats, food, toys): ')

# if supplyCategory in petShop['supplies']:
#     item = input(f'Enter the {supplyCategory} item to update: ')

#     if item in petShop['supplies']['habitats']:
#         continue  
# else:
#     print("Invalid supply category")

# 3. Calculate the total number of animals in the shop
totalAnimals = 0

# for animalType in petShop['animals']:
#     for breed in petShop['animals'][animalType]:
#         count = petShop['animals'][animalType][breed]
#         totalAnimals = totalAnimals + count # totalAnimals += count

for (animalType, animalBreeds) in petShop['animals'].items():
    for (breed, count) in animalBreeds.items():
        totalAnimals = totalAnimals + count # totalAnimals += count

print('\nThe total number of animals in the shop is:', totalAnimals)

# 4. Find which animal type has the most variety
petShop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3},
        "birds": {"Parakeet": 4, "Canary": 3, "Cockatiel": 7}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}

# IN THE FIRST INTEPRETATION, "VARIETY" WOULD MEAN THE MOST NUMBER OF BREEDS
mostVariety = 'Dogs'
varietyCount = 4

for (foodType, animalBreeds) in petShop['supplies'].items():
    breedCount = len(animalBreeds.keys())

    if (varietyCount == 0 or breedCount > varietyCount):
        varietyCount = breedCount
        mostVariety = animalType.capitalize()

print(f'\n The animal with the most number of breeds is {mostVariety} at {varietyCount}')

# TODO: IN THE SECOND INTEPRETATION, "VARIETY" WOULD MEAN THE ANIMAL WITH THE MOST HEADCOUNT (AND NUMBER OF BREEDS)

# TODO: Create a shopping list of supplies that are low in stock (fewer than 10)

print('')
