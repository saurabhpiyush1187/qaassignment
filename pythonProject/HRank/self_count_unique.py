# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def totalOperations(st, length):
    lst_duplicate=[]
    lst_st = [str(x) for x in st]
    for i in range(length):
        num = lst_st.count(lst_st[i])
        lst_duplicate.append(num)
    set_num = list(set(lst_duplicate))
    count = len(set_num)
    print(count)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    st = "geeksforgeeks"
    l = len(st)
    # print(totalOperations(st, l))
    totalOperations(st,l)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
