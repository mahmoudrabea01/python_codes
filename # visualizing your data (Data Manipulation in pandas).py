# visualizing your data (Data Manipulation with pandas)

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

avocados = pd.read_csv('avocados.csv')  # imaginary DF

# ============================================

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

print(nb_sold_by_size)


# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind='bar')

# Show the plot
plt.show()

# ================================


# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()
print(nb_sold_by_date)

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot()  # will create a line chart for the sales over the time

# Show the plot
plt.show()

# =============================

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x='nb_sold', y='avg_price', kind='scatter',
              title='Number of avocados sold vs. average price')

# Show the plot
plt.show()

# ================================================================

# Histogram of conventional avg_price
avocados[avocados['type'] == 'conventional']['avg_price'].hist()

# Histogram of organic avg_price
avocados[avocados['type'] == 'organic']['avg_price'].hist()

# Add a legend
plt.legend(['conventional', 'organic'])

# Show the plot
plt.show()

plt.clf()

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

plt.clf()

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(
    bins=20, alpha=0.5)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(bins=20, alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

# ==================================

#### handling missing values ############################

# Import matplotlib.pyplot with alias plt
avocados_2016 = avocados[avocados['year'] == '2016']

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()

# =====================

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().sum())

print(avocados_complete.isna().any())

# ======================

# replace missing values

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()

# 33

# creating dataframe from dictionaries

# Create a list of dictionaries with new data


avocados_list = [
    {'date': '2019-11-03', 'small_sold': 10376832, 'large_sold': 7835071},
    {'date': "2019-11-10", 'small_sold': 10717154, 'large_sold': 8561348}
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

# ======================

# Create a dictionary of lists with new data
avocados_dict = {
    "date": ['2019-11-17', '2019-12-01'],
    "small_sold": [10859987, 9291631],
    "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)

#######################################

# read and write from and to CSV

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv('airline_bumping.csv')

# Take a look at the DataFrame
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby(
    'airline')[['nb_bumped', 'total_passengers']].sum()

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals['nb_bumped'] / \
    airline_totals['total_passengers'] * 10000

# Print airline_totals
print(airline_totals)

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values(
    'bumps_per_10k', ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv('airline_totals_sorted.csv')  # .to_csv()
