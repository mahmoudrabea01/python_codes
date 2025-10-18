# Project: Exploring NYC Public School Test Result Scores

# Which NYC schools have the best math results?

# import pandas
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

am = 0.8 * 800  # variable to calc.  the percentage of 80%

# will returen the dataframe thatl's met the condition
schools[schools['average_math'] >= am]

best_math_schools = schools[schools['average_math']
                            >= am][['school_name', 'average_math']]

best_math_schools.sort_values('average_math', ascending=False)

# this will return a sorted table that's been created from the condition and have two fields

# 3

# What are the top 10 performing schools based on the combined SAT scores?

schools['total_SAT'] = schools['average_math'] + \
    schools['average_reading'] + schools['average_writing']

top_10_schools = schools.sort_values('total_SAT', ascending=False)[
    ['school_name', 'total_SAT']].head(10)

print(top_10_schools)  # to get the top 10 schools in total sat

##########################################

# Which single borough has the largest standard deviation in the combined SAT score?

top_10_schools = schools.sort_values('total_SAT', ascending=False)[
    ['school_name', 'total_SAT']]

borough_stats = round(schools.groupby('borough')['total_SAT'].agg(
    total_SAT='count', average_SAT='mean',  std_SAT='std').reset_index(), 2)

largest_std_dev = borough_stats.sort_values('std_SAT', ascending=False).head(1)

print(largest_std_dev)
