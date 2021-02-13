# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    my_list = [12, 65, 54, 39, 102,
               339, 221, 50, 70]
    list_ans = list(filter(lambda x:(x%13==0),my_list))
    print(list_ans)

    my_list_str = ['apple','orange','purple','qqqq']
    my_list_str_3 ='Robert'
    str_vowel = ['a','e','i','o','u']
    str_vowel_2 = "aeiou"
    n = len(my_list_str)
    list_ans_2 = list(filter(lambda x:(x in str_vowel),my_list_str_3))
    lis_ans_3 = list(filter(lambda x:( x[0] in str_vowel),my_list_str))

    print(list_ans_2)
    print(lis_ans_3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
