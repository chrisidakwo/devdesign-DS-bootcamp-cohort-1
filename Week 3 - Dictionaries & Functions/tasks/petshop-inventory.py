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

## Task 1
# Your task is to dynamically update the quantity of a supply item after a sale.
# Request as much information from the user in order to know what product is to be sold.
# Print out your inventory after each sale.

print('')
# TODO: Use regex to strip extra space characters
# category = input('Enter the category (food/toys/habitats): ').strip().lower()
# print('')


# if category not in petShop['supplies']:
#     print('Invalid category')
# else:
#     item = input('Enter the item name: ').strip()
#     print('')
    
#     if item in petShop['supplies'][category]:
#         quantity = int(input('Enter the quantity: '))
#         print('')

#         stockQty = petShop['supplies'][category][item]

#         if quantity <= stockQty:
#             petShop['supplies'][category][item] = stockQty - quantity
#             print(f'Sold {quantity} {item}. Remaining stock: {petShop['supplies'][category][item]}')

#             print('')
#             print("******************* UPDATED INVENTORY *******************")
#             print(petShop['supplies'])
#         else:
#             print('Not enough stock available!')
#     else:
#         print('Item not found')
# 
# print('')


## Task 2
# Create a shopping list of supplies that are low in stock (fewer than 10)

# lowStock = {}

# for category, items in petShop['supplies'].items():
#     for item, quantity in items.items():
#         if quantity < 10:
#             lowStock[item] = quantity

# print('Low stock items', lowStock)

## Task 3
# Find which animal type has the most variety. Variety in this case means the animal with the most headcount and number of breeds.

maxVariety = 0
mostVariedAnimal = None

for type, breeds in petShop['animals'].items():
    numberOfBreeds = len(breeds.keys())
    headcount = sum(breeds.values())

    variety = numberOfBreeds + headcount

    if variety > maxVariety:
        maxVariety = variety
        mostVariedAnimal = type

print(f'The animal with the most variety is {mostVariedAnimal.capitalize()} at {maxVariety}')
