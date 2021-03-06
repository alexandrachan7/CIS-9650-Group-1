# CIS-9650-Group-1
Team members: Alexandra Chan, Lei Gao, Qian Li, Kiran Syed, Weiqian Wu, Yuqing Wu

## Project Ideas:
Assume our clients have a lot of money and would like to do some investments in real estate. They are seeking recommendations about the condos/houses with different characteristics.

## Questions we solved:
- What are the factors that affect the most on the selling price?
- From 2012 to 2015, which neighborhoods perform better over the other? From 2016 to 2019, which neighborhoods perform better over the other. And is there anything changing from the previous decade? 
- How can we predict sales price with similarity analysis based on different fields (eg: borough, year built, gross square feet, & total units)?
- How has the percentage of condos/houses in the boroughs fluctuated over the last 5 years (2015 - 2019)? And based on the data of the most recent year (2019), provide top 5 neighborhoods supplied most condos (or houses) for clients interested in condos (or houses).
- What are some of the population trends between communities in the 5 boroughs?
- What’s the distribution of 0 sale’s price? Is there any pattern that sale’s day related to a specific month or weekday?

## Approach:
The code will be written in Python, mainly in Pandas environment. We plan to build our code to run analysis based on different characteristics in the datasets. The program can be divided into two sections. In the first part, users will be requested to input some relevent information and the program will do the prediction accordingly. In the second part, our program will do further analysis for real estate industry from different aspects, which will allow clients to have more information for their investment decisions.

## Datasets:
### Dataset I: “All Boroughs 2012 - 2019.csv”
It contains annual sales price data by borough in NYC from 2012 to 2019. Each year the data has around 1,000,000 records on 21 fields such as sales price, zip code, residential unit, gross square feet and year built etc.
Link: https://www1.nyc.gov/site/finance/taxes/property-annualized-sales-update.page

### Dataset II: “DOF__Cooperative_Comparable_Rental_Income__Citywide_(Report Year is Included).csv”
It contains condominiums or cooperatives valuation and valuation of rental properties similar in physical features and location to the condominiums or cooperatives from 2012 to 2019. It has around 40,000 records on 60 fields such as zip code, gross square feet and year built, and net operating income etc. In the context of our project, we used the data for condominium properties and not their corresponding rental properties.
1=Manhattan, 2=The Bronx, 3=Brooklyn, 4=Queens, 5=Staten Island
Link: https://data.cityofnewyork.us/City-Government/DOF-Cooperative-Comparable-Rental-Income-Citywide-/myei-c3fa


### Dataset III: “New_York_City_Population_By_Community_Districts.csv”
It contains census data from the different districts of the 5 boroughs of New York City between the years 1970 to 2010. 
Link: https://data.cityofnewyork.us/City-Government/New-York-City-Population-By-Community-Districts/xi7c-iiu2 

