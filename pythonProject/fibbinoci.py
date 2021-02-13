# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_n_fib(n):
    if n<=1:
        return n
    else:
        return print_n_fib(n-1) + print_n_fib(n-2)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    n=7
    #print nth fib number
    a = print_n_fib(n)
    print(a)
    m=7
    for i in range(0,m+1):
        print(print_n_fib(i))
    #print first fib series till m

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
