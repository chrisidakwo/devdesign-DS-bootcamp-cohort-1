import csv

FILENAME = 'Week 5 - Advanced File Handling/files/house_prices_semi.csv'

with open(FILENAME, 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)