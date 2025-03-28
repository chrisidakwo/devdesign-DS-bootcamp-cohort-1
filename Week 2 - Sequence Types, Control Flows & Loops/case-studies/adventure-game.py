# You are developing a simple text-based adventure game where the player explores a forest, 
# collects items, makes decisions, and encounters challenges.

# Game Setup:
# 1. The player starts with 100 health points (hp = 100) and an empty inventory (inventory = []).
# 2. They will explore different locations and make choices that affect their health and inventory.
# 3. The game continues until the player either reaches the final destination or their health drops to 0.

# Tasks
# Welcome the player and ask for their name.
# Store their starting health and an empty list for their inventory.
# Print a message showing the starting health and inventory.
# Display a message: “You arrive at a fork in the road. Do you go left or right?”
# Ask the player to choose a path (left or right).
# If they choose left, they find a health potion (adds +20 HP).
# If they choose right, they face a wild animal and lose -30 HP.
# If they enter any other response, they lose -10HP.
# Display updated health and inventory.
# The player finds a treasure chest with random items.
# Items could be any one of "Sword", "Shield", or "Gold Coins".
# Use a loop to allow the player to pick two items and add to inventory
# Display a message: “You reach a raging river. How will you cross?”
# If the player has a Shield, they safely cross.
# If they have a Sword, they fight off danger but lose 20 HP.
# If they have neither, they lose 50 HP while crossing.
# Use comparison and logical operators to determine the outcome.
# Display final HP.
# If HP is above 0, the player wins! Otherwise, it’s game over.

import random # Modules in Python

healthPoint = 100
inventory = []
locations = []
treasureChest = ["Sword", "Shield", "Gold Coins"]

print('')

name = input('Welcome! Please enter your name: ')

print('')
print('-----------------------------------------')
print(f"---- HEALTH: {healthPoint} || Inventory: {', '.join(inventory) if len(inventory) > 0 else 'Empty'} ----")
print('-----------------------------------------')
print('')


print('You arrive at a fork in the road. Do you go left or right?')
path = input('Choose a path (left or right): ')

if path == 'left':
    healthPoint = healthPoint + 20 # healthPoint += 20
elif path == 'right':
    print('Oops! You encountered a wild animal and lost 30 health points!')
    healthPoint = healthPoint - 30 #healthPoint -= 30
else:
    print('Oops! Invalid choice! You\'ve lost 10 health points!')
    healthPoint = healthPoint - 10 #healthPoint -= 10

print('')
print('-----------------------------------------')
print(f"---- HEALTH: {healthPoint} || Inventory: {', '.join(inventory) if len(inventory) > 0 else 'Empty'} ----")
print('-----------------------------------------')
print('')
    
# Helps to randomize the treasure items in the treasureChest list
treasureChest = ["Shield", "Sword", "Gold Coins"]
random.shuffle(treasureChest)

itemsAdded = 0
while (itemsAdded < 2):
    inventory.append(treasureChest[len(inventory)])
    itemsAdded = itemsAdded + 1  # itemsAdded += 1

print('You reach a raging river. How will you cross?')

if 'Shield' in inventory:
    print('Yay! You\'ve safely crossed the river!')
elif 'Sword' in inventory:
    healthPoint = healthPoint - 20
else:
    healthPoint = healthPoint - 50

# if 'Shield' in inventory:
#     print('Yay! You\'ve safely crossed the river!')

# if 'Sword' in inventory:
#     healthPoint = healthPoint - 20

# if (not 'Shield' in inventory) and (not'Sword' in inventory):
#     healthPoint = healthPoint - 50

print('')
print('-----------------------------------------')
print(f"---- HEALTH: {healthPoint} || Inventory: {', '.join(inventory) if len(inventory) > 0 else 'Empty'} ----")
print('-----------------------------------------')
print('')

if healthPoint > 0:
    print('You win!')
else:
    print('Too bad! Game over!')

print('')