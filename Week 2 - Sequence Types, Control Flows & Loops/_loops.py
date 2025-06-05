# A structure that allows you to repeat a block of code a number of times

# The number of times a loop runs can be determined by the following:
# - Type of loop
# - The length of items in the iterable
# - Outside influence (using a flag variable)


def main():
    numbers = [2, 4, 6, 8, 10]

    # For loop lets you traverse through an iterable
    # When you kow how many times you want to repeat something
    for num in numbers:
        print(num)

    print('\nUsing While Loop\n')

    # Used when you want to repeat something so long as the condition (boolean expression) remains true
    count = 0
    while count < 5:
        print(numbers[count])
        count = count + 1


if __name__ == '__main__':
    main()

