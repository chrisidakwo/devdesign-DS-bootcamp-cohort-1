import csv
import pprint

FILENAME = './files/house_prices.csv'

if __name__ == '__main__':
    housePricing = []

    with open(FILENAME, 'r') as file:
        csvReader = csv.reader(file)

        for row in csvReader:
            print(row)  # row is a list of values

        print('\n')

        # Dictionary reader - maps headers to values
        # file.seek(0)  # Go back to the beginning of the file
        #
        dictReader = csv.DictReader(file)
        for row in dictReader:
            housePricing.append(row)  # row is a dictionary {header: value}
            print(row)
