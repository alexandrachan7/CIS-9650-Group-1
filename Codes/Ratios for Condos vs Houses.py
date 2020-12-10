# How has the percentage of condos/houses in the boroughs fluctuated over the last 5 years (2015-2019)?

import pandas as pd
df = pd.read_csv("AllBoroughs2012-2019.csv")

import matplotlib.pyplot as plt

df["BOROUGH"]= df["BOROUGH"].replace(1, "Manhattan")
df["BOROUGH"]= df["BOROUGH"].replace(2, "Bronx")
df["BOROUGH"]= df["BOROUGH"].replace(3, "Brooklyn")
df["BOROUGH"]= df["BOROUGH"].replace(4, "Queens")
df["BOROUGH"]= df["BOROUGH"].replace(5, "Staten Island")
    
condos = df[(df["BUILDING CLASS AT PRESENT"] == "A3") | (df["BUILDING CLASS AT PRESENT"] == "A4") | (df["BUILDING CLASS AT PRESENT"] == "A5") | (df["BUILDING CLASS AT PRESENT"] == "A9")
            | (df["BUILDING CLASS AT PRESENT"] == "B1") | (df["BUILDING CLASS AT PRESENT"] == "B2") | (df["BUILDING CLASS AT PRESENT"] == "B3")
            | (df["BUILDING CLASS AT PRESENT"] == "C0") | (df["BUILDING CLASS AT PRESENT"] == "C1") | (df["BUILDING CLASS AT PRESENT"] == "C2") | (df["BUILDING CLASS AT PRESENT"] == "C3")]

houses = df[(df["BUILDING CLASS AT PRESENT"] == "R0") | (df["BUILDING CLASS AT PRESENT"] == "R1") | (df["BUILDING CLASS AT PRESENT"] == "R2") | (df["BUILDING CLASS AT PRESENT"] == "R3") | (df["BUILDING CLASS AT PRESENT"] == "R4") | (df["BUILDING CLASS AT PRESENT"] == "R6") | (df["BUILDING CLASS AT PRESENT"] == "R7") | (df["BUILDING CLASS AT PRESENT"] == "R8") | (df["BUILDING CLASS AT PRESENT"] == "R9")]

# Display the ratio of condos and houses for each borough from 2015 to 2019
num_condos = condos[condos["Sale Year"] >= 2015].groupby(["Sale Year", "BOROUGH"]).count()["ADDRESS"]
num_houses = houses[houses["Sale Year"] >= 2015].groupby(["Sale Year", "BOROUGH"]).count()["ADDRESS"]

ratio = num_condos / num_houses
print("Ratios between condos and houses for NYC's 5 boroughs from 2015 to 2019:")
print(ratio)
ratio.plot.bar(color=['red', 'blue', 'purple', 'green', 'orange'])
plt.title("Ratios between condos and houses for NYC's 5 boroughs (2015 - 2019)")
plt.xlabel("Sale Year, Borough")
plt.ylabel("Ratio")
plt.show()

# Based on the data of the most recent year (2019), provide top 5 neighborhoods supplied most condos/houses for clients interested in condos/houses
print("\nIn 2019, the top 5 neighborhoods supplied most condos are listed below:")
current_condos = condos[condos["Sale Year"] == 2019].groupby(["BOROUGH", "NEIGHBORHOOD"]).count()["ADDRESS"]
print(current_condos.sort_values(ascending = False).head(5))

print("\nIn 2019, the top 5 neighborhoods supplied most houses are listed below:")
current_houses = houses[houses["Sale Year"] == 2019].groupby(["BOROUGH", "NEIGHBORHOOD"]).count()["ADDRESS"]
print(current_houses.sort_values(ascending = False).head(5))























'''
#s_ratio = ratio.sort_values(["Sale Year", "ADDRESS"], ascending=[True, False])["ADDRESS"]
#maxR = ratio.groupby("Sale Year").nlargest(5)
#print(maxR)

#.sort_values(["Year", "Medal"], ascending=[True, False])["Medal"]
#print(ratio.sort_values(["Sale Year"], ascending = False)["ADDRESS"])

filtered_df = df.drop(df[(df["SALE PRICE"] == 0) | (df["SALE PRICE"] == "0") 
                         | (df["SALE PRICE"] == " -   ") | (df["SALE PRICE"] == " $-   ") 
                         | (df["TOTAL UNITS"] == 0) | (df["TOTAL UNITS"] == "0")
                         | (df["TOTAL UNITS"] == " -   ")
                         | (df["LAND SQUARE FEET"] == 0) | (df["LAND SQUARE FEET"] == "0")
                         | (df["GROSS SQUARE FEET"] == 0) | (df["GROSS SQUARE FEET"] == "0")].index)
new_df = filtered_df.dropna(subset=["TOTAL UNITS"])
print(len(new_df))

print(len(df[df["SALE PRICE"] == " $-   "]))

# Still exist discrepancies between filtered_df vs the filtered csv 
                                    #new_df vs the filtered csv

#df[df["SALE PRICE"] == " -   "]
#df[(df["TOTAL UNITS"] == 0) | (df["TOTAL UNITS"] == "0")]
#df[df["TOTAL UNITS"] == " -   "]
#df[(df["LAND SQUARE FEET"] == 0) | (df["LAND SQUARE FEET"] == "0")]
#df[(df["GROSS SQUARE FEET"] == 0) | (df["GROSS SQUARE FEET"] == "0")]

| (df["SALE PRICE"] == "-")
& (df["TOTAL UNIT"] == 0)
                 & (df["TOTAL UNIT"] == "-")
                 & (df["LAND SQUARE FEET"] == 0)
                 & (df["GROSS SQUARE FEET"] == 0)

demand = df.groupby("NEIGHBORHOOD")# .count()["TOTAL UNITS"].tolist()
years = df["Sale Year"]
print(len(years))
# print(demand.sum() / len(demand))



'''


























