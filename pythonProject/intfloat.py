# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    a ="9"
    b = int(a)
    c = float(b)
    print(c)

    pstr_old_state = {'a':'5', 'b':'6'}
    pstr_new_state = {'a':'5', 'b':'6'}

    bln_r = all(pstr_new_state[k] == v for k, v in pstr_old_state.items() if k in pstr_new_state)
    print(bln_r)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
