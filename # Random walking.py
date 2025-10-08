# Random walking

# # pip install numpy    ------ run this code on cmd or powershell to install numpy lib.
# # pip install matpoltlib    ------ run this code on cmd or powershell to install matplotlib lib.

# import numpy as np
# print(np.__version__)   # run this code to make sure it's been installed

# try:
#     import matplotlib.pyplot as plt
#     print("Matplotlib is installed")
# except ImportError:
#     print("Matplotlib is NOT installed") # to check if plt is installed or not
# ==============================================================

# import numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt

# # help(plt.hist) #help to show the histogram argument

# set a seed
np.random.seed(100)

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 1000 times
all_walks = []

# run a for loop
for w in range(1000):
    rand_walk = [0]  # set a list to run the if cond. on it
    for x in range(100):
        # to make sure that's the step start from the end step
        step = rand_walk[-1]
        dice = np.random.randint(1, 7)  # to create int number from 1 to 6
        if dice <= 2:
            step = max(0, step - 1)  # no nigative number allowed
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        if np.random.rand() <= 0.005:  # a chance to fall down
            step = 0

        rand_walk.append(step)

    all_walks.append(rand_walk)
# make sure that's all blocks are aliens correct

all_walks_np = np.array(all_walks)  # to tans it to array

# to make all steps aliens with each other
all_walks_np_t = np.transpose(all_walks_np)

# Select last row from all_walks_np_t: last_all_walks_np_t
last_all_walks_np_t = all_walks_np_t[-1, :]

# plot the result
plt.hist(last_all_walks_np_t)

# customize the chart
title = 'the distribution of steps'
ylable = '# of steps'
xlable = 'steps'

#######
plt.title(title)
plt.ylabel(ylable)
plt.xlabel(xlable)

# show the result
plt.show()

# print the odds that's will give you the persentage of reaching 70 steps or above
p = np.sum(last_all_walks_np_t >= 70) / 1000 * 100
print(f' the persentage of reaching 70 steps or above is : {p}')
