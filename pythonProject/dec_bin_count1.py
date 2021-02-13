# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    dec=6
    i=1
    bin1 =0
    while(dec>0):
        rem = dec%2
        dec= dec//2
        bin1 = bin1 + (i*rem)
        i = i*10
    print(bin1)
    dec1=6
    bin2 =bin(dec1)
    print(bin2)
    print(len(max(bin(dec1)[2:].split('0'))))
    lst_bin = [int(x) for x in str(bin1)]
    print(lst_bin)
    count =0
    result =0
    for i in range(len(lst_bin)):
        if lst_bin[i]==0:
            count =0
        else:
            count+=1
            result= max(result,count)
    print(result)

    str_lst_bin = list(map(str,lst_bin))
    print(str_lst_bin)
    s =[str(i) for i in str_lst_bin]
    res="".join(s)
    resultint= int(res)
    print(resultint)
    print(res)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/






