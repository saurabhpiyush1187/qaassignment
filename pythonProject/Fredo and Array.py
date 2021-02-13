# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    a = int(input())
    lst = list(num for num in input().strip().split())[:a]
    lst_int = [int(x) for x in lst]
    print(lst_int)
    sum =0
    for i in range(len(lst)):
        sum += lst_int[i]
    print(sum)

    avg = sum//len(lst_int)
    min = avg +1
    print(min)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
