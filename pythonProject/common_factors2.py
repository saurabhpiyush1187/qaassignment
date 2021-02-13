# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from math import sqrt


# Write your code here


# Function to calculate gcd of two numbers
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# Function to calculate all common divisors
# of two given numbers
# a, b --> input integer numbers
def commDiv(a, b):
    # find GCD of a, b
    n = gcd(a, b)
    print("gcd is " + str(n))

    # Count divisors of n
    result = 0
    for i in range(1, int(sqrt(n)) + 1):

        # if i is a factor of n
        if n % i == 0:

            # check if divisors are equal
            if n / i == i:
                result += 1
            else:
                result += 2

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a, b = str(input()).split(' ')
    a, b = int(a), int(b)
    print(commDiv(a, b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
