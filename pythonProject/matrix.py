# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    a=[]
    matrix=[]
    for i in range(R):
        a = list(int(num) for num in input().strip().split())[:C]
        matrix.append(a)
    print("=================")
    print(a)
    print("=================")
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], end=" ")
        print()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/






