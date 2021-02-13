# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    St = 'hi "my name is saurabh" and what "is yours"'
    print(St)
    str_final =''
    dbQuote = False
    for i in range(len(St)):
        if(St[i]==" " and not dbQuote):
            str_final+='\n'
        elif St[i]=='"':
            dbQuote = not dbQuote

        str_final+=St[i]

    print(str_final)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




