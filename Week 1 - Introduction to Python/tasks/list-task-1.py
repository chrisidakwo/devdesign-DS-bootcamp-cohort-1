# Task 1: 
# Create a list called movies with at least five of your favourite movie titles.
# Use an appropriate list method to add a new movie to the list.
# Replace the second movie in the list with a different one. Update the list accordingly.
# Print the updated movie list.
# Retrieve and print the last movie in the list using negative indexing.

movies = ["Black Hawk Down", "The Godfather", "Extraction", "Dark Knight", "The Shawshank Redemption"]
movies.append("The Pursuit of Happiness")

movies[1] = "Sniper Elite"

print(movies)

# You can access the items in a list/tuple using negative indexing
# The last item would always have an index of -1
lastItem = movies[-1]

print(lastItem)
