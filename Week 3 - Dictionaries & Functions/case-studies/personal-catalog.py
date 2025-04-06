import pprint

library = {
    "The Hobbit": {
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "Fantasy",
        "read": True,
    },
    "Dune": {
        "author": "Frank Herbert",
        "year": 1965,
        "genre": "Fiction",
        "read": False,
    },
}

print('')
print('MY LIBRARY', library)

# 1. Add a new book to your collection
library['Things Fall Apart'] = {
    'author': 'Chinua Achebe',
    'year': 1958,
    'genre': 'Fiction',
    'read': False
}

# An alternative way to add new items to a dictionary
# library.update({
#     'Things Fall Apart': {
#         'author': 'Chinua Achebe',
#         'year': 1958,
#         'genre': 'Historical Fiction',
#         'read': False,
#     },
# })

# 2. Mark "Dune" as read
library['Dune']['read'] = True

# Using the update() method
# library['Dune'].update({
#     'read': True,
# })

# 3. Print all books in a specific genre
print('')
specificGenre = "Fiction"

print(f"PRINT ALL BOOKS IN THE **{specificGenre.lower()}** GENRE")
print('')

for (bookName, bookDetails) in library.items():
    if bookDetails['genre'] == specificGenre:
        print(f"- {bookName} by {bookDetails['author']}")

print('')

print('GROUP BOOKS BY THEIR GENRE')
print('')

books = {}

for (bookTitle, bookDetails) in library.items():
    genre = bookDetails['genre']

    if genre in books:
        books['Fiction'].append(bookTitle)
    else:
        # books.update({ genre: [bookTitle] })
        books[genre] = [bookTitle]

for genre, bookNames in books.items():
    print(f"{genre}:", bookNames)

print('')

# 4. Create a "to read" list of all unread books
library.update({"The Book Thief": {
    'author': "Markus Zusak",
    'year': 1905,
    'genre': 'Fiction',
    'read': False
}})

print('')

# 4
booksToRead = []

for (bookTitle, bookDetails) in library.items():
    isRead = bookDetails['read']

    if (isRead is False):
        booksToRead.append(bookTitle)

print("HERE ARE THE BOOKS TO READ")
print(booksToRead)

# 5. Find the oldest book in your collection
oldestYear = 2025
oldestBook = ''

for (bookName, bookDetails) in library.items():
    if (bookDetails['year'] < oldestYear):
        oldestYear = bookDetails['year']
        oldestBook = bookName

print('')
print(f"THE OLDEST BOOK IS {oldestBook}, PRINTED IN {oldestYear}")

print('')
