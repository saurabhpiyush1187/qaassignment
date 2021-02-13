# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    user_in = short_string("My name is Saurabh\n what's your")
    print("shortest word is " + str(user_in))

def short_string(string):
    list_str = string.split(' ')
    list_str.sort(key=len)
    print(list_str)
    return list_str[0]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
