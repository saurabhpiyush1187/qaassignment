# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    reverse_string("My name is Saurabh what's your")

def reverse_string(str):
    list_words = str.split(' ')
    list_words.reverse()
    print(list_words)
    result = ' '.join(list_words)
    print(result)
    str_ex = list_words[0]
    print("Original Word" + str_ex)
    str_ex2 = str_ex[::-1]
    print(str_ex2)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
