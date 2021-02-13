# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    pdict_name = {
        "saurabh": 96,
        "aka": 98,
        "pdict": 100,
        "wers": 101,
        "ijuk": 100,
        "ujyh": 100
    }
    reverse_dict_keys(pdict_name)
    sort_dict(pdict_name)

def reverse_dict_keys(dict1):
    v = dict1.values()
    print("type of v is " + str(type(v))) #v is dict_values
    dec_sorted = sorted(list(set(v)), reverse= True)[1]
    second_highest = []

    for key, value in dict1.items():
        if value==dec_sorted:
            second_highest.append(key)

    second_highest.sort()

    print(second_highest)

def sort_dict(pdic1):
    sorted_keys = sorted(pdic1.keys(), reverse = True)
    print("Priting and sorting keys")
    print(sorted_keys)

    sorted_values = sorted(pdic1.values(), reverse=True)
    print("Priting and sorting values")
    print(sorted_values)

    sorted_dict_key = sorted(pdic1.items())
    print("Priting and sorting dict via keys")
    print(sorted_dict_key)

    sorted_dict_value = sorted(pdic1.items(),  key=lambda x: x[1])
    print("Priting and sorting dict via values")
    print(sorted_dict_value)

def basic_dict():
    dict1 ={}
    dict1["name"]='saurabh'
    dict1["class"] = 5
    dict1["age"] = 15
    dict1["roll"] = 1000

    print(dict1)
    dict1.pop("name")
    print(dict1)
    lst_values = dict1.values()
    print(lst_values)

    sort_dict(dict1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    basic_dict()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
