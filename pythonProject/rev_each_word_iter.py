# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    reverse_string("My name is Saurabh what's your")

def reverse_string(string):
    word = ''
    all_words = []
    string = string + ' '
    for i in range(0,len(string)):
        if string[i]!= ' ':
            word = word + string[i]
        else:
            all_words.append(word)
            word = ''
    all_words.reverse()
    final = ' '.join(all_words)
    print(final)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
