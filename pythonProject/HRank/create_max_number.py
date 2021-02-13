# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Python program to print the maximum number
# from the set of digits of a given number


# Function to print maximum number

def printMaximum(inum):
    # Hashed array to store count of digits

    count = [0 for x in range(10)]

    # Converting given number to string

    string = str(num)

    # Updating the count array

    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] + 1

    # Result stores final number

    result = 0

    multiplier = 1

    # traversing the count array

    # to calculate the maximum number

    for i in range(10):

        while count[i] > 0:
            result = result + (i * multiplier)

            count[i] = count[i] - 1

            multiplier = multiplier * 10

    # return the result

    return result
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    num = 38293367

    print(printMaximum(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
