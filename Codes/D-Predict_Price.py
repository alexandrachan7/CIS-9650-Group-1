import pandas as pd

df = pd.read_csv('AllBoroughs2012-2019.csv', usecols = ['BOROUGH','BUILDING CLASS CATEGORY','GROSS SQUARE FEET','YEAR BUILT','SALE PRICE','Sale Year']) #only read in certain row


df = df[(df['YEAR BUILT']!='') & (df['SALE PRICE'].str.isnumeric() == True) & (df['GROSS SQUARE FEET'].str.isnumeric() == True) & (df['BUILDING CLASS CATEGORY'] != "") & (df['YEAR BUILT'] != 0)]



df['SALE PRICE'] = df['SALE PRICE'].astype(float) #convert from object to float
df['GROSS SQUARE FEET'] = df['GROSS SQUARE FEET'].astype(float) 


df = df[(df['SALE PRICE'] >= 70000) & (df['GROSS SQUARE FEET']>= 500) & df['BUILDING CLASS CATEGORY'].str.contains('FAMILY',na=True)] #filter the row


#create new column based on BUILDING CLASS CATEGORY
numofFamily = []

for n in df['BUILDING CLASS CATEGORY']:
    if 'ONE' in n:
         numofFamily.append(1)
    elif 'TWO' in n:
         numofFamily.append(2)       
    elif 'THREE' in n:
         numofFamily.append(3)      
         
df['numofFamily'] = numofFamily #add new series to dataframe


desiredborough=int("2") #User enters the desired borough 1=Manhattan, 2=The Bronx, 3=Brooklyn, 4=Queens, 5=Staten Island)
desirednumofFamily=int("2") #User enters the total units) 1= one family house, 2=two family house, 3=three family house
desiredgrosssquare= int("1209")#User enters the gross square)
desiredyearbuilt= int("2010") #User enters the year built)

#desiredborough=int(input("1=Manhattan, 2=The Bronx, 3=Brooklyn, 4=Queens, 5=Staten Island\nPlease enter your Desired borough:"))
#desirednumofFamily=int(input("\n1=one family house, 2=two family house, 3=three family house\nPlease enter the number of family:"))
#desiredgrosssquare= int(input("Please enters the gross square:"))
#desiredyearbuilt= int(input("Please enters the year built:"))


########
#find closest number 
def findClosest(target,iList):
    diff = 999999
    for i in iList:
        d = abs(i-target)
        if  d < diff:
            diff = d
            result = i
        else:
            continue
    return result

########

#get dataframe of row meet the condituin
res =  df[(df['BOROUGH'] == desiredborough) & (df['numofFamily'] == desirednumofFamily)] #return dataframe

#get dataframe of row meet the condituin
resu = res[(res['GROSS SQUARE FEET'] == findClosest(desiredgrosssquare,res['GROSS SQUARE FEET']))]

print("\n..........Searching................")

#get dataframe of row meet the condituin
result = resu[(resu['YEAR BUILT'] == findClosest(desiredyearbuilt,resu['YEAR BUILT']))]

# caculate avaerge 
avgSQPrice = result['SALE PRICE']/result['GROSS SQUARE FEET']

######## get house ratio based  on 2018 and 2019

housePrice18 = df[(df['Sale Year'] == 2018)]['SALE PRICE'].sum() 
housePrice19 = df[(df['Sale Year'] == 2019)]['SALE PRICE'].sum() 

percentage = (housePrice18)/((housePrice19))

## predict the price 
pprice = desiredgrosssquare * avgSQPrice * (1+percentage)
print("Avgerage Sale price per square Feet: ", avgSQPrice.to_string(index=False), "\nIncrease Percentage: ", percentage)
print("The Estimate Price is ", pprice.to_string(index=False))