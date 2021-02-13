# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    lst_1 = [1,3,5,7,9]
    lst_2 = [2,4,8,10,11,15]
    res=[]
    i, j=0,0

    n = len(lst_1)
    m= len(lst_2)

    while i<n and j<m:
        if lst_1[i] < lst_2[j]:
            res.append(lst_1[i])
            i+=1
        else:
            res.append(lst_2[j])
            j+=1

    res = res+ lst_1[i:] + lst_2[j:]

    print(res)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
