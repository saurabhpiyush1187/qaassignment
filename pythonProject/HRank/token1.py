# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    St = input()

    # # for r in re.findall(r'".+?"|[\w-]+', S):
    # #     print (Send ="\n")
    #
    # # temp=[]
    # # temp.append(S.split("\""))
    # # print(temp)
    #
    str_n =re.findall(r'[^"\s]\S*|".+?"', St)
    for out in str_n:
        print(out)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




