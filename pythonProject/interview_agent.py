# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    data1 = [("Customer",1),("Agent",3),("Customer",5),("Customer",7),("Agent",9),("Customer",10),("Agent",13)]
    # list_diff = calculate_average(data1)
    # print(list_diff)
    customer=[]
    agent =[]
    for k in range(len(data1)):
        if "Customer" in data1[k]:
            customer.append(data1[k])
        elif "Agent" in data1[k]:
            agent.append(data1[k])

    list1 =[]
    prev_agent=0
    for i in range(0,len(customer)):
        c= customer[i]
        var = next(a for a in agent if a[1]>c[1] )
        cvar = (c[1], var[1])

        if prev_agent < c[1]:
            list1.append(cvar)
        prev_agent = var[1]
    print(list1)

    diff_list1=[]
    for l in range(len(list1)):
        difference = list1[l][1] - list1[l][0]
        diff_list1.append(difference)

    print(diff_list1)
    result = sum(diff_list1) / len(diff_list1)
    print(result)



def calculate_average(data1):
    max = 0
    min =0
    diff =0
    list_diff = []
    data1.insert(0,(("Agent",0)))
    lent = len(data1)-1
    for i in range(lent,-1,-1):
        if "Agent" in data1[i]:
            max = data1[i][1]
            for j in range(i-1,-1 ,-1):
                if (data1[j][0]== "Agent"):
                    min = data1[j+1][1]
                    diff = max- min
                    list_diff.append(diff)
                    min =0
                    max =0
                    diff =0
                    break

    return(list_diff)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
