# pandas summary statistics

# import pandas as pd
import pandas as pd

# import csv as DataFrame (imaginary DF)
sales = pd.read_csv('sales.csv')

# Print the head of the sales DataFrame
print(sales.head())  # Display the first few rows

# Print the info about the sales DataFrame
print(sales.info())  # the info about the columns

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())

# # Efficient summaries
# A custom IQR function


def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))

# print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l",
      "unemployment"]].agg([iqr, 'median']))

# THE RESULT SHOULD LOOK LIKE THIS
#         temperature_c  fuel_price_usd_per_l  unemployment
# iqr         16.583333              0.073176         0.565
# median      16.966667              0.743381         8.099

# ===============================

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# ===================

# # counting & removing duplicate

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())  # to remove dup. from DF

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')

# Print date col of holiday_dates
print(holiday_dates)

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts['department'].value_counts(
    sort=True, normalize=True)
print(dept_props_sorted)

# ###################### calc. each type by total

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "b"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# ======================
# # use groupby will give you the same result

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales['weekly_sales'])
print(sales_propn_by_type)

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg(
    ['min', 'max', 'mean', 'median'])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[
    ['unemployment', 'fuel_price_usd_per_l']].agg(['min', 'max', 'mean', 'median'])

# Print unemp_fuel_stats
print(unemp_fuel_stats)

# #===============
# using pivot table in group by

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')

# Print mean_sales_by_type
print(mean_sales_by_type)

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(
    values='weekly_sales', index='type', aggfunc=['mean', 'median'])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday
mean_sales_by_type_holiday = sales.pivot_table(
    values='weekly_sales', index='type', columns='is_holiday')

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='weekly_sales',
      index='department', columns='type', fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department",
      columns="type", fill_value=0, margins=True))
