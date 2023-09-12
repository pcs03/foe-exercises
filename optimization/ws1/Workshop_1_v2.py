# -*- coding: utf-8 -*-
"""
WORKSHOP 1 : Programming
FOE 3 - Year 4
@author: Alejandro Murrieta-Mendoza

Please help your colleagues and friends if they need assistance. 

This script is not graded.
The line codes here are just a proposed solution. You can implement your own solution 

Objectives:

    1.- Use pre-defined functions.
    2.- Compute the distance and initial azimuth between two cities <-- Directly 
        related to the assignment
    3.- Plot a waypoint
Version 2:
- Practice exercies removed and mixed to introduction to programming workshop. 
- Adjacent List created. 
"""
import numpy as np

# 1.- Download the function vinc.py from brightspace and place it in the SAME
#     directory as where this file is placed. You also need to import file from
#     function. What do yo think this file is doing?. Feel free to open it
#     and to take a look at it.
from vinc import v_direct, v_inverse

# 2.- Observe how the function is used
# boston = (lat,long) - Longitudes west of Greenwish are negative.
boston = (42.3541165, -71.0693514)
newyork = (40.7791472, -73.9680804)
x = v_direct(boston, newyork)  # In m and degrees
print("The distance between Boston and New York is: " + str(x[0]) + " m.")
print("The initial azimuth  between Boston and New York is: " + str(x[1]) + " degrees")

# 3.- Find the coordinates of Schipol, Los Angeles (LAX), and Narita (NAA)
#     remember to find them in degrees.
AMS = (52.308055555555555, 4.764166666666667)
NAA = (35.765277777777776, 140.38555555555556)
LAX = (33.94249722222222, -118.40805)

zero = (30, 0.00001)
zn = (30, 180)


# 4.- Use the imported function v_direct to find the distances between AMS - LAX,
#     AMS - NAA, and LAX-NAA in meteres, kilometers and nautical miles.
#     Print the results

LAX_NAA = v_direct(zero, zn)  # In m and degrees
print("The distance between Los Angeles and Narita is: " + str(LAX_NAA[0]) + " m.")
print("The initial azimuth between Los Angeles and Narita is: " + str(LAX_NAA[1]) + " degrees")


# 5.- Plot the waypoints as a scatter plot.

# 6 .- Assign random distance values to trajectories 1 to three and use an embeded IF
#      statement to find the longest one. Try different combinations to test your
#      logic.

# trajectory_1 = ___
# trajectory_2 = ___
# trajectory_3 = ___

# if ___:
#     if ___:
#         ___
#     else:
#         ___
# else:
#     if ___:
#         ___
#     else:
#         ___


# 7.- Open the Figure_1.png from Brigthspace. You are traveling from point A to point Z.
#     1.- Create an adjacent matrix showing the connections between different nodes.
#         Think about how that adjacent matrix will be used. How does the algorithm know where
#         "to go" next.
#     Hint: You can rename your points to make it easier to make it easier to identify and
#            visualize in your adjancent matrix.

# 8.- This is a short workshop. If you have not finished the exercises, this is a good moment to do so.
# *** WORKSHOP 1 ENDS ***
