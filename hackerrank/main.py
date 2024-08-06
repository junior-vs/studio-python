# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_weird():
    print(f'Weird')  # Press Ctrl+F8 to toggle the breakpoint.


def print_not_weird():
    print(f'Not Weird')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Escolha um numero')
    n = int(input().strip())

    if n % 2:
        print_weird()
    elif 2 <= n <= 5:
        print_not_weird()
    elif 6 <= n <= 20:
        print_weird()
    elif n >= 20:
        print_not_weird()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
