# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    n=[1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1]
    # n=[0,0,0,0,0,0,0,0]
    # n=[1,1,1,1,1]
    pstr_one=[]
    one =0
    # for i in range(len(n)):
    #     if n[i] == 1:
    #         one = one +1
    #         if i == len(n)-1:
    #             pstr_one.append(one)
    #     if n[i] == 0:
    #         if n[i-1] !=0:
    #             pstr_one.append(one)
    #             one = 0
    # pstr_one.sort(reverse=True)
    # if len(pstr_one)!=0:
    #     k = pstr_one[0]
    # else:
    #     k=0
    # print(pstr_one)
    # print(k)
    result =0
    for i in range(len(n)):
        if n[i]==0:
            one =0
        else:
            one+=1
            result= max(result,one)

    print(result)










# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/






