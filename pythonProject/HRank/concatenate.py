# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def FindIt(N, ch):
    lst_name = list(ch)
    str_name = ''.join(lst_name)
    return str_name

def FindIt_new(N, ch):
    temp=""
    for i in range(N):
        if ch[i]!=" ":
            temp+=ch[i]
    return temp


# Write your code here


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    N = int(input())
    ch = input().split()[:N]

    out_ = FindIt(N, ch)
    print(out_)

    out__ = FindIt_new(N, ch)
    print(out__)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
