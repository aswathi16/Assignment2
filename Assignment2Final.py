# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 13:03:16 2022

@author: Aswathi
"""

#importing requiredpackages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def read_file(file_name):
    """
        This function takes name of the file and reads the file and loads it into a dataframe.
        Then transposes the dataframe and returns both the first and transposed dataframes
    """

    df = pd.read_csv(file_name)
    df_transpose = pd.DataFrame.transpose(df)
    return(df, df_transpose)

#Reads the files
df_Forest_total,df_forest_countries = read_file("Forest_Area.csv")
df_totalPopulation_total,df_totalPopulation_countries = read_file("Total_Population.csv")
df_urbanPopulation_total,df_urbanPopulation_countries = read_file("Urban_Population.csv")
df_co2_total, df_co2_countries = read_file("CO2_Emission.csv")



"""
Forest Area used bar graph
Creating bar graph of Forest area in sq.km in mutiple countries from 1990-2015
"""

#Header setting
header = df_forest_countries.iloc[0].values.tolist()
df_forest_countries.columns = header

#Cleaning the dataframe
df_forest_countries = df_forest_countries.iloc[1:]
df_forest_countries = df_forest_countries.iloc[11:55]

#Converting index to int
df_forest_countries.index = df_forest_countries.index.astype(int)
df_forest_countries = df_forest_countries[df_forest_countries.index>1989]
df_forest_countries = df_forest_countries.dropna(axis = 'columns')

#Creates a list of countries to use in the plot
countries =[ 'United Kingdom','India','United States', 'China', 'Germany', 'Canada', 'France', 'Bangladesh']
df_forest_time = pd.DataFrame.transpose(df_forest_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]

#selecting only required data
df_forest_subset_time = df_forest_time[years].copy()
df_forest_subset_time = df_forest_subset_time.loc[df_forest_subset_time.index.isin(countries)]

#plotting the data
n=8
r=np.arange(n)
width= 0.1
plt.bar(r-0.3, df_forest_subset_time[1990], color = 'grey',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_forest_subset_time[1995], color = 'g',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_forest_subset_time[2000], color = 'orange',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_forest_subset_time[2005], color = 'red',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_forest_subset_time[2010], color = 'steelblue',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_forest_subset_time[2014], color = 'black',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Forest Area")
plt.xticks(width+r, countries, rotation = 45)
plt.legend()
plt.title("Forest area(Sq. Km)")
#plt.savefig("line1.png", dpi=300, bbox_inches='tight')
plt.savefig("Forest Area.png", dpi=300, bbox_inches='tight')
plt.show()

   



    
"""
total population bar graph
Creating bar graph of total population of multiple countries from 1990-2014
"""
header = df_totalPopulation_countries.iloc[0].values.tolist()
df_totalPopulation_countries.columns = header

#Cleaning the dataframe

df_totalPopulation_countries = df_totalPopulation_countries.iloc[1:]
df_totalPopulation_countries = df_totalPopulation_countries.iloc[11:55]

df_totalPopulation_countries.index = df_totalPopulation_countries.index.astype(int)
df_totalPopulation_countries = df_totalPopulation_countries[df_totalPopulation_countries.index>1989]

df_totalPopulation_countries = df_totalPopulation_countries.dropna(axis = 'columns')

df_totalPopulation_time = pd.DataFrame.transpose(df_totalPopulation_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]
df_totalPopulation_subset_time = df_totalPopulation_time[years].copy()
df_totalPopulation_subset_time = df_totalPopulation_subset_time.loc[df_totalPopulation_subset_time.index.isin(countries)]

#plotting the data
plt.bar(r-0.3, df_totalPopulation_subset_time[1990], color = 'aqua',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_totalPopulation_subset_time[1995], color = 'turquoise',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_totalPopulation_subset_time[2000], color = 'steelblue',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_totalPopulation_subset_time[2005], color = 'deepskyblue',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_totalPopulation_subset_time[2010], color = 'blue',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_totalPopulation_subset_time[2014], color = 'navy',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Total Population")
plt.xticks(width+r, countries, rotation = 45)
plt.legend()
plt.title("Total Population")
plt.savefig("Total_Population.png", dpi=300, bbox_inches='tight')
plt.show()






"""
Urban Population bar graph
Creates a bar chart of Urban Population of multiple countries during 1990-2014
"""


header = df_urbanPopulation_countries.iloc[0].values.tolist()
df_urbanPopulation_countries.columns = header

#Cleaning the dataframe

df_urbanPopulation_countries = df_urbanPopulation_countries.iloc[1:]
df_urbanPopulation_countries = df_urbanPopulation_countries.iloc[11:55]

df_urbanPopulation_countries.index = df_urbanPopulation_countries.index.astype(int)
df_urbanPopulation_countries = df_urbanPopulation_countries[df_urbanPopulation_countries.index>1989]

df_urbanPopulation_countries = df_urbanPopulation_countries.dropna(axis = 'columns')

df_urbanPopulation_time = pd.DataFrame.transpose(df_urbanPopulation_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]
df_urbanPopulation_subset_time = df_urbanPopulation_time[years].copy()
df_urbanPopulation_subset_time = df_urbanPopulation_subset_time.loc[df_urbanPopulation_subset_time.index.isin(countries)]

#print(df_energy_subset_time[1995])

#plotting the data
plt.bar(r-0.3, df_urbanPopulation_subset_time[1990], color = 'pink',width = width, edgecolor = 'black',label='1990')
plt.bar(r-0.2, df_urbanPopulation_subset_time[1995], color = 'deeppink',width = width, edgecolor = 'black',label='1995')
plt.bar(r-0.1, df_urbanPopulation_subset_time[2000], color = 'coral',width = width, edgecolor = 'black',label='2000')
plt.bar(r, df_urbanPopulation_subset_time[2005], color = 'khaki',width = width, edgecolor = 'black',label='2005')
plt.bar(r+0.1, df_urbanPopulation_subset_time[2010], color = 'yellow',width = width, edgecolor = 'black',label='2010')
plt.bar(r+0.2, df_urbanPopulation_subset_time[2014], color = 'greenyellow',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Urban Population)")
plt.xticks(width+r, countries, rotation = 45)
plt.legend()
plt.title("Urban Population")
plt.savefig("urbanPopulation.png", dpi=300, bbox_inches='tight')
plt.show()


"""
Lineplot gdp per capita
Creates a lineplot of CO2 Emission of multiple countries during 1990-2014.
Used mean to fill empty cells
"""

header = df_co2_countries.iloc[0].values.tolist()
df_co2_countries.columns = header

#Cleaning the dataframe
df_co2_countries = df_co2_countries.iloc[1:]
df_co2_countries = df_co2_countries.iloc[11:55]

df_co2_countries.index = df_co2_countries.index.astype(int)
df_co2_countries = df_co2_countries[df_co2_countries.index>1990]

#using mean() function of pandas to fill empty cells of Canada and Bangladesh
canada_mean =df_co2_countries["Canada"].mean()
bangladesh_mean = df_co2_countries["Bangladesh"].mean()

df_co2_countries["Canada"].fillna(canada_mean, inplace = True)
df_co2_countries["Bangladesh"].fillna(bangladesh_mean, inplace = True)

#plotting the data
plt.figure()
plt.plot(df_co2_countries.index, df_co2_countries["India"])
plt.plot(df_co2_countries.index, df_co2_countries["United Kingdom"] )
plt.plot(df_co2_countries.index, df_co2_countries["Canada"])
plt.plot(df_co2_countries.index, df_co2_countries["China"])
plt.plot(df_co2_countries.index, df_co2_countries["France"])
plt.plot(df_co2_countries.index, df_co2_countries["Bangladesh"])
plt.plot(df_co2_countries.index, df_co2_countries["Germany"])
plt.plot(df_co2_countries.index, df_co2_countries["United States"])
plt.xlim(1991,2014)
plt.xlabel("Year")
plt.ylabel("co2 Emission")
plt.legend(["India", "UK", "Can", "Ch", "Fr", "Ban", "DE", "US"])
plt.title("CO2 Emission")
plt.savefig("co2.png", dpi = 300, bbox_inches='tight')
plt.show()

