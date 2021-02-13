# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #phone number must start with 789 and should be of 10 digits
    #input
    # 2
    # DEXTER < dexter @ hotmail.com >
    # VIRUS < virus!@variable.:p >
    n = int(input())
    lst_n = []
    for i in range(n):
        item = input().strip()
        lst_n.append(item)

    for i in range(len(lst_n)):
        res = bool(re.match(r'\b(\w+)\s<[^-._][\.a-zA-Z0-9_-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', lst_n[i]))
        if res == True:
            print(lst_n[i])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




