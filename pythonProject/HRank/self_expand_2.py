# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import shlex
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    str_num = input()
    str_n = shlex.split(str_num)
    for i in range(len(str_n)):
        if " " in str_n[i]:
            str_n[i] = "\"" + str_n[i] + "\""

    for out in str_n:
        print(out)

    str_new = shlex.split(str_num,posix=False)
    for out in str_new:
        print(out)










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
