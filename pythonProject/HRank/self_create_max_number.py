# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Python program to print the maximum number
# from the set of digits of a given number


# Function to print maximum number

def printMaximum(inum):
 lst_num = [int(x) for x in str(num)]
 lst_int_sorted = sorted(lst_num,reverse=True)
 lst_str_sorted = map(str,lst_int_sorted)
 str_num = [str(i) for i in lst_str_sorted]
 res = "".join(str_num)
 final_number = int(res)
 return final_number


if __name__ == '__main__':
    print_hi('PyCharm')
    num = 38293367

    print(printMaximum(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
