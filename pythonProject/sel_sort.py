# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    list_unsorted = [6,8,4,3,9,1]
    selec_sort(list_unsorted)

def selec_sort(lst):
    for i in range(len(lst)):
        min_indx = i
        for j in range(i+1,len(lst)):
            if(lst[min_indx] > lst[j]):
                min_indx = j

        lst[i],lst[min_indx] = lst[min_indx],lst[i]

    print(lst)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
