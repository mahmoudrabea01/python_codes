# expilict index (Data Manipulation with pandas)

import pandas as pd

import numpy as np

temperatures = pd.read_csv('temperatures.csv')  # imiginary DataFrame

# =====================

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# subsetting using Loc[]

# Make a list of cities to subset on
cities = ["London", "Paris"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(
    level=('country', 'city'), ascending=(True, False)))

# 33

# slicing and subsetting with .loc and .iloc[]

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Philippines
print(temperatures_srt.loc['Pakistan': 'Philippines'])

# Try to subset rows from Lahore to Manila
print(temperatures_srt.loc['Lahore': 'Manila'])  # This will return nonsense.

# Subset rows from Pakistan, Lahore to Philippines, Manila
print(temperatures_srt.loc[('Pakistan', 'Lahore'): ('Philippines', 'Manila')])

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'): ('Iraq', 'Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, 'date': 'avg_temp_c'])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad')      : ('Iraq', 'Baghdad'), 'date': 'avg_temp_c'])

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(
    temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-31')]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010': '2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['2010-08': '2011-02'])

# slicing using iloc[]

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22][1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[: 5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2: 4])

# Use slicing in both directions at once
print(temperatures.iloc[0: 5, 2: 5])

########################################

# working with pivot tables

# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(
    'avg_temp_c', index=['country', 'city'], columns='year')

# See the result
print(temp_by_country_city_vs_year)

# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt': 'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'): ('India', 'Delhi')]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'): (
    'India', 'Delhi'), '2005': '2010']

# cul. the mean

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])  # year
# 2013    20.312285
# dtype: float64

print(mean_temp_by_year[mean_temp_by_year.idxmax()]
      )                    # 20.312285

print(mean_temp_by_year[mean_temp_by_year.sort_values(
    ascending=False).index[0]])   # 20.312285


# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city ==
      mean_temp_by_city.min()])  # country  city
# China    Harbin    4.876551
#  dtype: float64
