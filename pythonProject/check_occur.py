# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    check_string("My name is Saurabh\n what's your",'yps')

def check_string(o_str,str_check):
    for i in range(0,len(str_check)):
        count = 0
        flag=0
        for j in range(0,len(o_str)):
            if str_check[i] == o_str[j]:
                flag=1
                count = count + 1
                print("Location for  " + str_check[i] + " found at " + str(j+1) + " location")
        if flag ==0:
            print(str_check[i] + " character not found in the ori string")
        print("Total count for " + str_check[i] + " is " + str(count))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
