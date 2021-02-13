# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    leap(2012)

def leap(year):

    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))

    if (year % 4) == 0 and ((year%100 != 0) or (year%400 == 0)):
        print(str(year) + " is a leap year" )
    else:
        print(str(year) + " is not a leap year")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
