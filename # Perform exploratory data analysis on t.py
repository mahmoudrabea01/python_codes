# Perform exploratory data analysis on the netflix_data.csv
# data to understand more about movies from the 1990s decade.
# ======== a project of netflix films on DataCamp


# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# What was the most frequent movie duration in the 1990s?

duration = int(netflix_df[netflix_df['release_year'].between(1990, 1999)]
               ['duration'].mode())


print(duration)  # ==== the result is 94

print('#' * 60)

# A movie is considered short if it is less than 90 minutes.
# Count the number of short action movies released in the 1990s
# and save this integer as short_movie_count.

short = netflix_df[(netflix_df['duration'] < 90) & (netflix_df['release_year'].between(1990, 1999))
                   & (netflix_df['genre'] == 'Action')]

short_movie_count = short['duration'].count()

print(short_movie_count)            # ===== the result is 7
