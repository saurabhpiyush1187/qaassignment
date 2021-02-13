# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    list_unsorted = [6,8,4,3,9,1]
    result = bina(list_unsorted,0)
    if result !=-1:
        print("Item found")
    else: print("item not found")

def bina(lst,item):
    n = len(lst)
    right = n-1
    left = 0

    while(left <= right):
        middle = (left+right)//2
        if(item== lst[middle]):
            return middle
        if(item>lst[middle]):
            left= middle+1
        else:
            right = middle-1
    return -1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
