# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import math

from PIL import Image, ImageDraw
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    point1 = [1, 2]
    point2 = [3, 4]

    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]

    plt.plot(x_values, y_values)
    plt.show()

    w, h = 220, 190
    shape = [(40, 40), (w - 10, h - 10)]

    # creating new Image object
    img = Image.new("RGB", (w, h))
    # create line image
    img1 = ImageDraw.Draw(img)
    img1.line(shape, fill="none", width=0)
    img.show()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




