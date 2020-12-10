#Question: From 2012 to 2015, which neighborhoods perform better over the other? From 2016 to 2019, which neighborhoods perform better over the other. 
#And is there anything changing from the previous decade? (use dataset II)
#what are the top 3 neighborhoods for 2012 - 2015 and 2016 - 2019?
import pandas as pd
df = pd.read_csv("DOF__Cooperative_Comparable_Rental_Income__Citywide_.csv")

#to filter out blank value
df["Net Operating Income"].fillna(0, inplace = True)
df["Full Market Value"].fillna(0, inplace = True)

#split the dataset into two parts and filter out 0 for NOI and FMV
ff = df[(df["Report Year"] <= 2015)&(df["Report Year"] >= 2012)&(df["Net Operating Income"] >0)&(df["Full Market Value"] > 0)]
gf = df[(df["Report Year"] <= 2019)&(df["Report Year"] >= 2016)&(df["Net Operating Income"] >0)&(df["Full Market Value"] > 0)]

#what are the top 3 neighborhoods for 2012 - 2015?
avgnoi = ff.groupby(["Neighborhood", "Borough Name"])["Net Operating Income"].mean()
afmv = ff.groupby(["Neighborhood", "Borough Name"])["Full Market Value"].mean()
caprate1215 = avgnoi/afmv

print("Top 3 neighborhoods for 2012 - 2015")
print(caprate1215.nlargest(3))
nbs = ff["Neighborhood"].unique()

#what are the top 3 neighborhoods for 2016 - 2019?
avnoi = gf.groupby(["Neighborhood", "Borough Name"])["Net Operating Income"].mean()
avfmv = gf.groupby(["Neighborhood", "Borough Name"])["Full Market Value"].mean()
caprate1619 = avnoi/avfmv
print("")
print("Top 3 neighborhoods for 2016 - 2019")
print(caprate1619.nlargest(3))






