# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def totalOperations(st, length):
    # Dictionary to store characters and their frequencies
    d = {}
    for i in range(length):

        # If already contains the character then
        # increment its frequency by 1
        if st[i] in d:
            d[st[i]] += 1

        # Else add the character to the HashMap with frequency 1
        else:
            d[st[i]] = 1

    # Set to Store unique frequency
    valueSet = set()

    # Insert frequencies into HashSet
    for key in d.keys():
        valueSet.add(d[key])

        # Count of unique frequencies
    return len(valueSet)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    st = "geeksforgeeks"
    l = len(st)
    print(totalOperations(st, l))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
