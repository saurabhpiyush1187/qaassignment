# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print(ord('P')-ord('P'))
    a = input()
    lst = str(a).split(' ')
    lst_int = [int(x) for x in lst]

    lst[0], lst[1] = lst[1], lst[0]

    a1 = int(lst[0]) * int(lst[2])
    b1 = int(lst[1]) + int(lst[2])
    print(str(a1) + ' ' + str(b1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
