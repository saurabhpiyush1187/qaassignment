# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print_n_prime(10)

def print_n_prime(n):
    c=0
    pno=2
    while(c<n):
        flag=0
        if(pno==2):
            print(str(pno) + " is the prime number")
            c= c+1
            pno = pno +1
        else:
            for i in range(2,pno):
                if pno%i == 0:
                    flag=1
                    pno = pno+1
                    break
            if flag==0:
                print(str(pno) + " is the prime number")
                c = c + 1
                pno = pno + 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
