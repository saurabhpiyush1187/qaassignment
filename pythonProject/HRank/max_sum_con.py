# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    lst_num = [2,3,4,1,90,4,98]
    n=3
    lst_max = []
    i=0
    while(i+n<=len(lst_num)):
        Sum = sum(lst_num[i:i+n])
        lst_max.append(Sum)
        i+=1
    print(lst_max)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
