#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

V2. Weather exercises included
This is finally the last one of all

Same old, follow the instrutions, try to think what have been done before,
how can you adapt that to your new problem?

"""

import numpy as np
##============================================================================
## Exercise 1
## Go to brightspace and open the file Graph_Exercise.pdf
## Develop an algorithm that prints all the possible combinatins of trajectories
## on the downloaded file that connects the point AMS to FCO (Rome)
## Save ALL the options in a list.
##============================================================================
graphs = [[0,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
#This is the adjacent matrix (you are welcome)


##============================================================================
## Exercise 2
## Now that you have all the possible trajectories. 
## 1.- Find the main aiport coordinates for each city at Graph_Exercise.pdf
## 2.- Compute the distance for each edge of the graph. 
## 3.- Assign random wind and find the shortest trajectory (using the wind)
## 4.- Assume an altitude of 34,000 ft and a Mach = 0.74. What is the flight
##     time for each possible flight? 
##     Remember that the Mach number to TAS changes with the altitude. 
## 5.- What would be the flight time for each trajectory with the wind?
## 6.- Assign wind to a trajectory so the solution would be
##     AMS - PRAGUE - MILAN - ROME
## Speed of sound = sqrt(gamma * R * T)
## Where gamma = 
##============================================================================


##============================================================================
## Exercise 3
## Using the same data as in workshop 2
## Develop an algorithm that makes a random decision on what waypoint
## it should follow next. Print the final distance. Print the real distence and the wind distance
##============================================================================


##============================================================================
## Exercise 4
## Real weather predictions
## Place the files:
## 1.- TMP_date_1_alt_1.csv
## 2.- WIND_date_1_alt_1.csv
## 3.- WDIR_date_1_alt_1.csv
## Uncomment the code below line by line. 
## Understand what it is happening
## Read and understand the code below
##============================================================================
# This line below loads the funciton
# import load_weather from load_weather
# This line below extracts the weather information from the csv files (of course you can chagne your function)
# tmp, wind, wdir = load_weather()
"""
 Explanation: 
     tmp = temperature (Kelvin)
     wind = wind speed (knots)
     wdir = wind direction. 0 is North. (Degrees)
     The World is separated in a grid where the first waypont is
     defined to be at 90 S, 180 W. Or the lower left corner as in 
     https://weather.gc.ca/grib/global222.png. 
     The distance between every point is 0.6 degrees for the lateral and
     longitudinal coordinates. 
     For this reason, this variables do not provide real coordinates 
     but indeces.
     The Columns names for the variables tmp, wind and wdir are as follows:
     |i index| j index| value|
     i index refers to the longitude, j index to the latitude and value is the 
     desired data: temperature, wind speed or wind direction.
     
     For example, the value:
         i index = 1   j index = 1  corresponds to 90S 180W or (0, 0)
         i index = 2   j index = 1 corresponds to 90S  179.4W or (0,0.6)
         i index = 1   j index = 2 corresponds to 89.4S 180W or (0.6,0)
     
    The 360 degrees of longitude are divided in 601 points. 
    The 180 degrees of latitde are divided in 301 points
    
    Official website:
        https://weather.gc.ca/grib/grib2_glb_66km_e.html
    
    The procedure below helps you indentify a close value for a given
    coordinate (51.5039, -0.12574) - (Lat, Lon)
"""


# LAT should be given from -90(SOUTH) to 90 (NORTH)
# LON shoould be provided from -180 (WEST) to 180 (EST)

# tmp = np.genfromtxt('TMP_date_1_alt_1.csv', delimiter = ',')
# wind = np.genfromtxt('WIND_date_1_alt_1.csv', delimiter = ',')
# wdir = np.genfromtxt('WDIR_date_1_alt_1.csv', delimiter = ',')

# lat =  51.5039
# lon = -0.12574


# lat = lat + 90 # real coordinate
# lat_i = lat/180
# lat_i = (lat_i * 301)
# lat_i = round(lat_i) # index


# lon = 180 + lon
     
# lon_i = lon/360
# lon_i = lon_i * 601
# lon_i = round(lon_i) # index

# The operation at row provides the row where the desired indeces are located
# row = (lat_i-1)*601+lon_i-1

# print("The required indeces are: ")
# print ("For i index (lon_i) :  " + str(lon_i))
# print ("For j index (lat_i) :  " + str(lat_i))

# print("The approximateive coordinate are: ")
# print ("Longitude :  " + str(lon_i*0.6)) # 0.6 as it is the separation
# print ("Latitude :  " + str(lat_i*0.6))
# print("")

# temperature_row = tmp[row]
# temperature = tmp[row][2]
# print ("The temperature row " + str(row) + " contains the following information:")
# print(temperature_row)
# print("")

# wind_speed_row = wind[row]
# wind_speed = wind[row][2]

# print ("The wind row " + str(row) + " contains the following information:")
# print(wind_speed_row)
# print("")

# wind_dir_row = wdir[row]
# wind_dir = wdir[row][2]

# print ("The wind dir row " + str(row) + " contains the following information:")
# print(wind_dir_row)
# print("")

"""
    Run the script.
    The results show that the row variable provide the required indices. 
    The temperature at the closest point to (51.5083,-0.12574)
    is 231.077 Kelvin, the wind speed is  6.0342 knots and 
    the wind angle is 249.5 degrees (North is 0 degrees)
    
    The coordiantes for the closest point are (142.2, 180)
    or: (142 - 90, 180-180)
        (52 N, 0 W) 
"""


##============================================================================
## Exercise 4
## Real weather predictions
## Obtain the temperature, the wind angle (from the ture north) and the wind speed from the trajectory
## in Trajectory_example.txt. (You have to load this to python).
## Extra challengue: Compute the ground speed given a Mach number of 0.82.
## TIP: You might want to encapsulate the code above in a function. 
##============================================================================


##============================================================================
## Exercise 5
## This is actually the end of the Workshops. Along with the optimization lecture.
## By this point you should be able to:
##  1.- Create an optimization problem.
##  2.- Model a problem into equations
##  3.- Use given functions for your proble
##      Example: Vincenty and weather
##  4.- Manipulate lists and numpy arrays. 
##  5.- Use built in functions in your benefit (Sum. min, max, etc)
##  6.- Compute the distance between waypoints. 
##  7.- Understand the difference between costs: real and fake distances. 
##  8.- Implement the simplest optimization algorithms to find a solution.
##  9.- Create your own waypoints using geodesic equations. 
## 10.- Plot your waypoints in a different enviornment.
## 11.- Load files into data frames
## 12.- Clean files
## 13.- Use the data frames to compute distances.
## 14.- Develop the logic to be able to execute a brute force algorithm (Execrise 1 here above)
## 15.- Use the simplest stochastic algorithm. 
## 16.- Use an adjacent table to represent graphs
## 17.- You will find a bunch of weather data for different altitudes and different days in Brightspace. 

## What are we missing? Graph representation. This will be up to you
## There are many options, you can se packages to model the graph or you
## can go old school and use pure adjacent lists/matrices (as done here.  
## This will be a challengue for you to solve. Feel free to take this  
## lesson in Datacamp: Network Analysis in Python (Part 1)
## https://www.datacamp.com/courses/network-analysis-in-python-part-1
## Or use class (type of data) or any tool that you might find interesting.  
## Rememeber that you must develop your own code to apply the shortest path
## algorithm. Do not be afraid to look for inspiration in other people's code
## For the rest you can use packages. 
##
## NO CODE should be delivered in the paper. No python exclusive terms should
## be used. Just follow the instructions provided in your Research methdology workshop. 

## Metaherusitic algorithms are also missing. They are fairly simple to code
## as long as you understand what they are doing. 
## In general:
## Do not be afraid to ask other teams for help, feedback, or other opinions.
## Help each other.
## 
## What is next?
## 1.- Pick your algorithm, code it and have fun.
## 2.- Write your paper with all the instructions and methdology provied in your
##     Research methdology workshop. The quality of the paper is graded. 
##============================================================================
