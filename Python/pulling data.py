import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():
    """jajajaj"""
    listed = []
    df = pd.read_csv("WOrlddd.csv", encoding = "UTF-8")
    df.index = df['Country Name']
    for i in df['Country Name'].head(5):
        listed.append(i)
    tmp = sorted(df['2016'].head(5))
    print(tmp)
    plt.plot(tmp)
    plt.show()
main()
