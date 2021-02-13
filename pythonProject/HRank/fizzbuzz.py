# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    n= int(input())
    lst_n = list(map(int,input().split()))[:n]
    print(lst_n)

    for ele in lst_n:
        for i in range(1, ele + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
                continue
            elif i % 3 == 0:
                print("Fizz")
                continue
            elif i % 5 == 0:
                print("Buzz")
                continue
            print(i)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




