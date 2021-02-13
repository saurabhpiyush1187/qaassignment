# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def expandString(strin):
    temp = ""
    j = 0
    i = 0
    while (i < len(strin)):
        if (strin[i] >= "0"):

            # Subtract '0' to convert char to int
            num = ord(strin[i]) - ord("0")
            if (strin[i + 1] == '('):

                # Characters within brackets
                j = i + 2
                while (strin[j] != ')'):
                    # if ((strin[j] >= 'a' and strin[j] <= 'z') or
                    #         (strin[j] >= 'A' and strin[j] <= 'Z')):
                    temp += strin[j]
                    j += 1

                # Expanding
                for k in range(1, num + 1):
                    print(temp, end="")

                # Reset the variables
                num = 0
                temp = ""
                if (j < len(strin)):
                    i = j
        i += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    strin = "3(ab)4(cd)"
    expandString(strin)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
