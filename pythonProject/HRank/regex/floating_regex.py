# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    n = int(input())
    # lst_n = list(num for num in input().split('\n'))[:n]
    lst_n=[]
    for i in range(n):
        item = input().strip()
        lst_n.append(item)

    for i in range(len(lst_n)):
        print(bool(re.match(r'^[0-9]+\.[0-9]+|^[+-][0-9]+\.[0-9]+',lst_n[i])))
    print(lst_n)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




