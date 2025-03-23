# You are developing a simple text-based adventure game where the player explores a forest, collects items, makes decisions, and encounters challenges.

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
# Display updated health and inventory
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

healthPoint = 100
inventory = []
locations = []
treasureChest = ["Sword", "Shield", "Gold Coins"]

name = input('Welcome! Please enter your name: ')
path = input('Please choose a path (left or right): ')