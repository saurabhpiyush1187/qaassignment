# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    lst_num = [2,3,4,1,90,4,98]
    k=3
    n = len(lst_num)
    i=0
    res = sum(lst_num[i:k])
    cur_sum =res
    for i in range(k,n):
        cur_sum+= lst_num[i] - lst_num[i-k]
        res =max(res,cur_sum)

    print(res)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
