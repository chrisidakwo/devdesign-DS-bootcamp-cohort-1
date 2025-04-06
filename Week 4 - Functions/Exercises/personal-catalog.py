libraryData = {
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

# 1. Add a new book to your collection
def addBookToCollection(bookName, author, year, genre, read = False):
    libraryData[bookName] = {
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

# 2. Mark a book as 'read'
def markBookAsRead(bookName):
    libraryData[bookName]['read'] = True

# 3. Print all books in a specific genre
def printAllBooksForGenre(genre):
    print(f"PRINT ALL BOOKS IN THE **{genre.lower()}** GENRE")
    print('')

    for (bookName, bookDetails) in libraryData.items():
        if bookDetails['genre'] == genre:
            print(f"- {bookName} by {bookDetails['author']}")

# 5. Find the oldest book in your collection
def retrieveOldestBook():
    oldestYear = 2025
    oldestBook = ''

    for (bookName, bookDetails) in libraryData.items():
        if (bookDetails['year'] < oldestYear):
            oldestYear = bookDetails['year']
            oldestBook = bookName

    return oldestBook


print('')
print('*************** LIBRARY ***************')
print(libraryData)
print('')

print('Task 1')
addBookToCollection('Things Fall Apart', 'Chinua Achebe', 1958, 'Fiction')

print(libraryData)
print('')

print('Task 2')
markBookAsRead('Dune')

print(libraryData)
print('')

print('Task 3')
printAllBooksForGenre('Fiction')

print('')

print('Task 5')
oldestBook = retrieveOldestBook()
print(f'The oldest book is {oldestBook}')
print()