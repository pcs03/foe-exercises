"""
V0: Creation
V1: New exercise: Recursive Function 
Objectives:
    a) Load a Data Frame
    b) Basic Data Frame Manipulation
    C) Basic Visualization
Please notice that the provided files are given in .xls (DATA on DLO)
1. Find a way to translate those files to .csv (not necesarily in Python)
2. Rename Flight 1 to flight_csv.csv
3. Follow the rest of this file.

@author: Alejandro Murrieta-Mendoza
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

##============================================================================
## Exercise 1
## Using the command read_csv and the help information (which can be found in
## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
## load the file flight_csv.csv.
## use print(data_frame.head()) to visualize your data
##============================================================================

df = pd.read_csv(os.path.abspath("./optimization/ws3/flight_csv.csv"))
print(df.columns)


##============================================================================
## Exercise 2
## Observe your variables in your data frame. Giving the goal of your assignment.
## Is there any variable (column) that you can drop (erase/remove) to make
## your dataframe a bit smaller? If so, drop it.
## It is always a good practicer to NEVER alter your original dataframe.
## For this reason, make a copy of your data frame and read how to drop columns
## https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
## For your assignment you should analyse what variables from your data frame
## are useful.
##============================================================================


##============================================================================
## Exercise 3
## For the rest of excercises, just leave the columns [3d Latitude],
## [3d Latitude]','[3d Longitude]','[3d Altitude Ft].
## Names are long and cumbersome. Once you have selected those values from
## the dataframe, rename them to LAT, LON, and ALT.
## Hint: df.rename()
## Print the first 10 values and the last 10 values. head() and tail() could
## be useful
## Also look at the functio df.describe()
##============================================================================


df = df.loc[
    :,
    [
        "[3d Latitude]",
        "[3d Longitude]",
        "[3d Altitude Ft]",
    ],
]
df = df.rename(columns={"[3d Latitude]": "lat", "[3d Longitude]": "lon", "[3d Altitude Ft]": "alt"})
print(df.head())
print(df.describe())

##============================================================================
## Exercise 4
## You may have noticed that there are values such as (lat,lon) = (0,0). This is
## evidently not correct. It might be because the navigation tool was not yet
## activated. Go ahead and remove those values from your dataframe.
## use .describe() and verify the max and min LAT,LON values.
## Do they make sense? What about the Altitude at Schiphol? Is the max altitude
## during flight realistic?
## When working with data sets it is always important to ask these questions.
## If you do not know, it is time to ask an expert about typical values.
## You can as well use the function .drop_duplicates() after to remove the
## The duplicated vales
##============================================================================

df = df[(df["lat"] > 0) & (df['lon'] > 0)]
print(df.describe())

##============================================================================
## Exercise 5
## Great, now we have a "clean" dataframe. Let us see how it looks like.
## Plot your altitude agains the waypoint #. (or the row index)
## What do you observe? (Do not read Exericse 6 just yet. Think about it)
##============================================================================

# fig, ax = plt.subplots()
# ax.plot(df.ALT[:])
# ax.set(xlabel='Waypoint #', ylabel='Altitude (ft)',
#        title='Flight Profile')
# fig.savefig("test.png")   # Only if you want to save the plot on y our HDD.
# ax.grid()
# plt.show()


##============================================================================
## Exercise 6
## You have tought about it?
## Then you have noticed that the first and the last
## waypoints are always at the same altitude . Why is that? Should you remove them?
## Just for fun let's remove them and plot the data again
## You might want to explore PANDASERIES.to_frame(), Transpose x.T
## and pd.conct(....).reset_index(drop = True) or any other way you might know
##============================================================================


##============================================================================
## Exercise 7
## As we are interested in the cruise only. Extract the cruise part from the
## Data frame. You might want to create new data frames for every flight phase.
## Plot the cruise phase
##============================================================================


##============================================================================
## Exercise 8
## It looks ugly now, does not it? These are real flights, it is hard to keep
## exact altitude. That is also the reason why there is vertical separation,
## to account for this errors. Extend the plot scale to reduce this effect.
## Hint: ax.set_ylim()
##============================================================================


##============================================================================
## Exercise 9
## Use the complete flight data (Ex 6) set and using vincenty, compute the total
## flight distance taking all points into account. Measure the computation time
## Create a list where you can also store the distance between waypoints.
##============================================================================


##============================================================================
## Exercise 10
## you might encouter that your waypoints are too close togetheter.
## Select 10 waypoints (Plus the initial two for a total of 12)
## Compute the distance between those waypoints. They should be the same.
## Measure the computation time
##============================================================================

# begin_ = time.perf_counter()
# YOUR CODE
# end_ = time.perf_counter()
# total_time = end_ - begin_

##============================================================================
## Exercise 11
## load the dataset named flightaware.txt avaiable in DLO
## You guessed it. I just copy and pasted this data from flightaware in a
## .txt file.
## Load this file to python
## Clean it
## Plot the complete flight
##============================================================================


##============================================================================
## Exercise 12
## Recursive function: Function that calls itself
## Example:
##============================================================================
def down_to_number(initial, n):
    print(initial)
    if initial == n:
        return  # Terminate recursion (Let's get out of here)
    else:
        initial -= 1
        down_to_number(initial, n)  # Recursive call


# Observe the behaviour closely, pat attention to recursive call
down_to_number(initial=10, n=1)

# Do you understand what it is happening?

##============================================================================
## Exercise 13
## Recursive functions: Function that calls itself
## Now try to think how to solve the typical example
## Find the factorial of a given number n by using a recursive function.
## n! = n × (n – 1) × (n – 2) × … × 1
##============================================================================


## END OF WORKSHOP

"""
If you look at the raw data, you can oberve that data is sampled every 0.25 seconds.
Another way of cleaning the data is to pick only integer values, in other words,
To reduce the sampling by 1 second. They you can apply the filters and cleaning
as did in thi document. 


Why am i torturing you with the recursive function? 
It might be helpful to solve the first exercise of the next workshop.
At least i solve it with that :) 
    
# Cool tool to observe your orientation if on doubt
# https://www.desmos.com/calculator/3e7iypw4ow


"""
