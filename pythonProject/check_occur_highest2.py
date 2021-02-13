# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    check_string("MyyyynunuaaisssisrrrrMk")
    # list1 = [(5,'i'),(8,'j'),(7,'o'),(2,'h')]
    # list1.sort()
    # print(list1)


def check_string(o_str):
    str_check = list(set(o_str))
    print(str_check)
    lst_char=[]
    for i in range(len(str_check)):
        count=(o_str.count(str_check[i]))
        var = (count, str_check[i])
        lst_char.append(var)
    lst_char2 = sorted(lst_char,reverse=True)
    char_lowest,literal = lst_char2[0]
    print(str(literal) + " is the highest occuring character\n")






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
