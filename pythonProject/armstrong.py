# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import logging

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
        lst_num = [370,3,121,1634,407,370]
        for i in range(len(lst_num)):
            sum=0
            temp = lst_num[i]
            order = len(str(lst_num[i]))
            while temp>0:
                digit = temp%10
                temp = temp//10
                sum += digit**order
            if lst_num[i] == sum:
                print(str(lst_num[i]) + " is a armstrong number")
            else:
                print(str(lst_num[i]) + " is not an armstrong number")




# Press the green button in the gutter to run the script.
if __name__== '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
