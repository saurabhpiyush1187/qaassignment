# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    str_num = "3(ab)4(bc)"

    temp=""
    i=0
    j=0
    while(i<len(str_num)):
        if str_num[i].isdigit():
            num = int(str_num[i])

            if str_num[i+1] == '(':

                j=i+2
                while (str_num[j]!= ')'):
                    temp+= str_num[j]
                    j+=1

                for k in range(num):
                    print(temp,end="")

                num =0
                temp=""
                if (j<len(str_num)):
                    i=j
        i+=1




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
