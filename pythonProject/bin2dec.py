# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    dec1=110
    dec=dec1
    bin=0
    i=1
    while(dec>0):
        rem= dec%10
        dec=dec//10
        bin= bin + (i*rem)
        i = i*2
    print("Binary conversion of " + str(dec1) + " is " + str(bin))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
