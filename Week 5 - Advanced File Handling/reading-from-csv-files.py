import csv
import pprint

FILENAME = 'Week 5 - Advanced File Handling/files/house_prices.csv'

housePricing = []

with open(FILENAME, 'r') as file:
    csvReader = csv.reader(file)

    for row in csvReader:
        print(row)  # row is a list of values

    print('\n')

    # Dictionary reader - maps headers to values
    file.seek(0)  # Go back to the beginning of the file

    dictReader = csv.DictReader(file)
    for row in dictReader:
        housePricing.append(row)  # row is a dictionary {header: value}

pprint.pprint(housePricing)