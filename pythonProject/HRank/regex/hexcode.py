# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #phone number must start with 789 and should be of 10 digits

    #input
    # 11
    # # BED
    # {
    #     color:  # FfFdF8; background-color:#aef;
    #         font - size: 123
    # px;
    # background: -webkit - linear - gradient(top,  # f9f9f9, #fff);
    # }
    # # Cab
    # {
    #     background - color:  # ABC;
    #         border: 2
    # px
    # dashed  # fff;
    # }

    reg = re.compile(r"(:|,| +)(#[abcdefABCDEF1234567890]{3}|#[abcdefABCDEF1234567890]{6})\b")
    reg = re.compile(r"(?<!^)(#(?:[\da-f]{3}){1,2})")

    n = int(input())

    for i in range(n):
        line = input()
        items = reg.findall(line)

        if items:
            for item in items:
                print(item[1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




