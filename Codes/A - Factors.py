
"""
Created on Wed Dec  9 22:36:45 2020

@author: kiransyed
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 10,5
import seaborn as sb

df = pd.read_csv("AllBoroughs2012-2019.csv")
print(df.head())

print(df.info())

cols = ['SALE PRICE',
        'GROSS SQUARE FEET',
        'LAND SQUARE FEET',
        'TOTAL UNITS',
        'COMMERCIAL UNITS',
        'RESIDENTIAL UNITS']

for col in cols:
    df[col] = df[col].apply(lambda x: str(x).replace("-","").strip())
    df[col] = df[col].apply(lambda x: str(x).replace("$","").strip())
    df[col] = df[col].apply(lambda x: str(x).replace("nan","0").strip())
    df[col] = df[col].apply(lambda x: str(x).replace(",","").strip())

for col in cols:
    df[col] = pd.to_numeric(df[col])

df['SALE DATE'] = pd.to_datetime(df['SALE DATE'])

print(df.info())

print(df.isna().sum())

df.corr()['SALE PRICE'].index
plt.bar(df.corr()['SALE PRICE'].index, df.corr()['SALE PRICE'])
plt.tight_layout()
plt.xticks(rotation=90)
plt.grid()
plt.title("Correlation of Sale Price VS other Factors", size=24)
plt.show()

sb.heatmap(df.corr(),annot=True,cmap="YlGnBu")

print(df['SALE DATE'].dt.year)

df.set_index(df['SALE DATE']).resample("Y").sum()["SALE PRICE"].plot()
plt.title("SUM(SALE PRICE) vs YEAR")
plt.show()

df.set_index(df['SALE DATE']).resample("M").sum()["SALE PRICE"].plot()
plt.title("SUM(SALE PRICE) vs MONTH")
plt.show()

df.set_index(df['SALE DATE']).resample("M").sum()["SALE PRICE"].plot()
df.set_index(df['SALE DATE']).resample("M").sum()["SALE PRICE"].rolling(10, win_type='gaussian').sum(std=0.5).plot()
plt.title("SUM(SALE PRICE) vs MONTH")
plt.legend(['SUM SALE PRICE', 'ROLLING MEAN OF WINDOW 10'])
plt.show()

sb.scatterplot(df['BOROUGH'], df['SALE PRICE'])
plt.xticks([1,2,3,4,5])
plt.show()

plt.figure(figsize=(30,5))
sb.scatterplot(df['BUILDING CLASS CATEGORY'], df['SALE PRICE'])
plt.xticks(rotation=90)
plt.show()

