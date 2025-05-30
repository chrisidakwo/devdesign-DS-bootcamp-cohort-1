from idlelib.configdialog import is_int

def add(a, b):
    if not is_int(a):
        raise TypeError('The first number must be an integer')

    if not is_int(b):
        raise TypeError('The second number must be an integer')

    return a + b


def main():
    sum = add(5, 8)
    print(f'The sum of 5 and 6 is {sum}')

if __name__ == '__main__':
    main()