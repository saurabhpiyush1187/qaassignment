# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    a, b = str(input()).split(' ')
    a, b = int(a), int(b)
    n = 0
    if a >= b:
        lim = a
    else:
        lim = b
    for num in range(1, lim):
        if a % num == 0 and b % num == 0:
            print(num, end = ' ')
            n += 1
    print(n)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
