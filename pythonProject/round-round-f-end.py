# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    input1 = input()
    lst = input1.split(' ')
    n = int(lst[0])
    k = int(lst[1])
    lst2 = list(int(num) for num in input().strip().split())[:n]
    a = [int(x) for x in lst2]
    k = n-k
    msg =" "
    for i in range(0,n):
        p = a [(i + (n-k))%n]
        msg = msg + str(p) + " "
        # print(str(p), end = " ")
    print(msg[1:])




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/






