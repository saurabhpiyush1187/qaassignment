# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    lst_one = [1,1,1,0,0,0,1,1,0,1,1]
    str_lst = ''.join([str(i) for i in lst_one])
    print(str_lst)
    str_split = (str_lst.split('0'))
    print(str_split)
    count = len(max(str_split, key=len))
    print(count)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
