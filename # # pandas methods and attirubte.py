# # pandas methods and attirubte
# # the DataFrames Are not downloaded it's just for show

# import pandas as pd
import pandas as pd

#################################################

# Print the head of the homelessness data
print(homelessness.head())  # the first few rows

# Print information about homelessness
print(homelessness.info())  # info about the DataFrame(thetable)

# Print the shape of homelessness
print(homelessness.shape)  # (num of rows , num of columns)

# Print a description of homelessness
print(homelessness.describe())  # some summary about the DataFrame

# Print the values of homelessness
print(homelessness.values)   # return the values of DF as arrays

# Print the column index of homelessness
print(homelessness.columns)  # name of columns

# Print the row index of homelessness
print(homelessness.index)   # num of indexs

#####################################

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending=False)

# return the first few rows in desc order from DF homelessness
print(homelessness_fam.head())

#####################################

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(by=['region', 'family_members'],
                                                ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())

######################################################

# Select the individuals column
individuals = homelessness['individuals']

print(individuals.head())       # the first rows of the col. individuals

########################

# Select the state and family_members columns
# the first rows of the cols state
state_fam = homelessness[['state', 'family_members']]
# & family_members

# note don't forget to put two [[]]
# first(outer) [] responsible for subsetting the DataFrame
# second(inner) [] creating a list of columns to subset

print(state_fam.head())

# ============================
# another exmple

# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals', 'state']]

print(ind_state.head())

####################################

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10000]

# See the result
print(ind_gt_10k)          # return the DataFrame with the condition

########################

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region'] == 'Mountain']

# See the result
print(mountain_reg)

print(ind_gt_10k & mountain_reg)  # to met the two condition

# # ============== or you can put it on one line but don't forget () for each condition ======

# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & (
    homelessness['region'] == 'Pacific')]

# See the result
print(fam_lt_1k_pac)

##############################

# subsetting using isin() method
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)

#################################

# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness[[
    'individuals', 'family_members']].sum(axis=1)

# ======= or
homelessness['total'] = homelessness['individuals'] + \
    homelessness['family_members']

# Add p_homeless col as proportion of total homeless population to the state population
homelessness['p_homeless'] = homelessness['total'] / homelessness['state_pop']

# See the result
print(homelessness)

##########################

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * \
    homelessness['individuals'] / homelessness['state_pop']

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values(
    'indiv_per_10k', ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result
print(result)
