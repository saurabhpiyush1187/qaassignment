# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    n=9
    ar = [10,10,20,10,20,9,10,9,10]
    result = sockMerchant(n, ar)
    print(result)

def sockMerchant(n, ar):
    new_ar= list(set(ar))
    actual_count = 0
    for i in range(len(new_ar)):
        temp = ar.count(new_ar[i])
        if temp>=2:
            count_s = temp // 2
            actual_count += count_s

    return actual_count



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
