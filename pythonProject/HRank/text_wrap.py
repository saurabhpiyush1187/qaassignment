# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def wrap(string, max_width):
    lst_wrap = []
    temp = ''
    return_s =''
    i = 0
    k = 0
    while (i < len(string)):
        temp += string[k:(i+max_width)]
        lst_wrap.append(temp)
        i = i+max_width
        k = i
        temp=''

    for out_ in lst_wrap:
        return_s+= out_ + "\n"

    return return_s


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width =4
    result = wrap(string, max_width)
    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
