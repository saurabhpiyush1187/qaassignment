# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    user_in = return_string()
    print(str(user_in)+'\n')
    list_str = user_in
    # list_str = [str(x) for x in str(user_in)]
    # print(list_str)
    count =0
    for i in range(len(list_str)):
        if list_str[i]=='q':
            break
        else:
            count = count +1
            print('count is' + str(count))
    print("Final count is " + str(count))


def return_string():
    while True:
        user_in = input("Press 1 to quit\n")
        if '1' in user_in: break
    return str(user_in)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
