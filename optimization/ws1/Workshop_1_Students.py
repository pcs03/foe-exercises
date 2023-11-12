# -*- coding: utf-8 -*-
"""
WORKSHOP 1 : Programming Optimisation
FOE COP - Year 4
@author: Alejandro Murrieta-Mendoza

Please help your colleagues and friends if they need assistance. 

This script is not graded.
The line codes here are just a proposed solution. You can implement your own solution 

Objectives:

    1.- Use pre-defined functions.
    2.- Compute the distance and initial azimuth between two cities <-- Directly 
        related to the assignment
    3.- Find a waypoint
Version 2:
- Practice exercises removed and mixed to introduction to programming workshop. 
- Adjacent List created. 
Version 3: 
- Adjacent List moved to next workshop
- Schiphol waypoint placement re-introduced. 
"""
import numpy as np



    
# 1.- Download the function vinc.py from brightspace and place it in the SAME
#     directory as where this file is placed. You also need to import file from
#     function. 
#     What do yo think this file is doing?. Feel free to open it
#     and to take a look inside. 
from vinc import v_direct

# 2.- Observe how the function is used    
# boston = (lat,long) - Longitudes west of Greenwich are negative. 
boston = (42.3541165, -71.0693514)
newyork = (40.7791472, -73.9680804)
x = v_direct(boston, newyork) # In m and degrees
print("The distance between Boston and New York is: " + str(x[0])+ " m.")
print("The initial azimuth  between Boston and New York is: " + str(x[1]) + " degrees")

# 3.- Find the coordinates of Schiphol, Los Angeles (LAX), and Narita (NAA)
#     remember to find them in degrees. 
ams_lat = ____
ams_lon = ____
AMS = (ams_lat, ams_lon)  # respect the order

naa_lat = ____
naa_lon = ____
NAA = (____, ____)

lalaland_lat = _____
lalaland_lon = _____
LAX = _____

# 4.- Use the imported function v_direct to find the distances between AMS - LAX, 
#     AMS - NAA, and LAX-NAA in meteres, kilometers and nautical miles. 
#     Print the results
naa_lat = 35.77
naa_lon = 140.38
NAA = (naa_lat, naa_lon)

lalaland_lat = 33.94252
lalaland_lon = -118.4071
LAX = (lalaland_lat, lalaland_lon)
LAX_NAA = v_direct(LAX, NAA) # In m and degrees
print("The distance between Los Angeles and Narita is: " + str(LAX_NAA[0]) + " m.")
print("The initial azimuth between Los Angeles and Narita is: " + str(LAX_NAA[1]) + " degrees")


# 5.- Plot the waypoints as a scatter plot.

# 6.- Get the coordinates of Schiphol.
#  Using a loop, obtain the coordinates located 200 nm North, East, West, South, North-East, North-West, South-East and South-West from 
#  Schiphol. Plot them.


# 7 .- Assign random distance values to trajectories 1 to three and use an embeded IF 
#      statement to find the longest one. Try different combinations to test your
#      logic.

trajectory_1 = ___
trajectory_2 = ___
trajectory_3 = ___

if ___:
    if ___ :
        ___
    else:
        ___
else:
    if ___:
        ___
    else:
        ___

# Can you find the longest distance from exercise 4 using the if schema?

# 8.- This is a short workshop. If you have not finished the exercises from the beginning nor follows the Datacamp courses, this is a good moment to do so. This serves as a reminder. What you learn here can also be applied to FOE 2. 
# *** WORKSHOP 1 ENDS ***