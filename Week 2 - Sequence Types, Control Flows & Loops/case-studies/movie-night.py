# You and your friends want to watch a movie, but there are two conditions:
# 1. You must have at least $10 to afford a ticket.
# 2. The movie should have at least a 7.5 rating on IMDb.

# Task:
# 1. Ask the user for the amount of money they have.
# 2. Ask the user for the IMDb rating of the movie.
# 3. Use comparison and logical operators to check if they can go to the movie.
# 4. Print "Enjoy your movie!" if they can afford it and it has a good rating. 
# Otherwise, suggest watching something at home.

print('')

amount = int(input('Enter the amount of money you have: '))
movieRating = float(input('Enter the movie rating: '))

if amount >= 10 and movieRating >= 7.5:
    print('Enjoy your movie!')
else:
    print('Why not watch something better at home!')

print('')