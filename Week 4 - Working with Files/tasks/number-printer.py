# Write a program that:
# 1. Creates a text file called "numbers.txt"
# 2. Writes numbers 1 to 50, one per line
# 3. Reads the file back
# 4. Calculates and prints the sum of all numbers in the file

# Additional attempts:
# - Allow the user to specify how many numbers to generate
# - Add error handling to your solution
# - Calculate other statistics (average, min, max)

FILENAME = 'Week 4 - Working with Files/files/numbers.txt'

def createFile(count = 50):
    file = open(FILENAME, 'w')

    for number in range(1, count + 1):
        file.write(f'{number}\n')

    file.close()


def readNumbersFromFile():
    file = open(FILENAME, 'r')

    numbers = []
    for line in file:
        numbers.append(int(line.strip()))

    file.close()

    return numbers


def calculateStatistics(numbers):
    # Calculate the sum
    totalSum = sum(numbers)

    # Calculate average
    average = totalSum / len(numbers)

    # Find minimum and maximum numbers
    minNumber = min(numbers)
    maxNumber = max(numbers)

    return (totalSum, average, minNumber, maxNumber)


print('')

count = int(input('How many numbers do you intend to generate? '))

createFile(count)

numbers = readNumbersFromFile()

# Option 1: Use index position to access the calculated stats
statistics = calculateStatistics(numbers)

print('\n************* STATISTICS *************')
print(f'Sum: {statistics[0]}')
print(f'Average: {statistics[1]}')
print(f'Minimum Number: {statistics[2]}')
print(f'Maximum Number: {statistics[3]}')

# Option2: you can unpack (destruct) the tuple and use variable names to access items in the tuple rather than their index position
# totalSum, average, minNum, maxNum = calculateStatistics(numbers)

# print('\n************* STATISTICS *************')
# print(f'Sum: {totalSum}')
# print(f'Average: {average}')
# print(f'Minimum Number: {minNum}')
# print(f'Maximum Number: {maxNum}')