# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    ans= count_iter("My name is Saurabh what's your","a")
    print(ans)

def count_iter(string,char):
    if not string:
        ans =0
    elif char == string[0]:
        ans = 1 + count_iter(string[1:], char)
    else:
        ans = count_iter(string[1:], char)
    return ans




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
