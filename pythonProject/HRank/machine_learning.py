# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

import matplotlib.pyplot as plt
import math
import numpy as np #n dim objct suport
from sklearn.cross_validation import train_test_split
df = pd.read_csv("./pima-data.csv")
from PIL import Image, ImageDraw
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    print(df.shape)
    print(df.head(5))
    print(df.tail(5))
    bool1 = df.isnull().values.any()
    print(bool1)
    plot_corr(df)
    plt.show()
    
def plot_corr(af, size=11):
    corr = af.corr() #dataframe corr func
    fig, ax = plt.subplots(figsize=(size,size))
    ax.matshow(corr) #color code the rectangle by correlation values
    plt.xticks(range(len(corr.columns)),corr.columns) #draw xtick marks
    plt.yticks(range(len(corr.columns)), corr.columns) #draw ytick marks


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




