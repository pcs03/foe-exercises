#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nov 2019
Workshop 3 - Part 1 (of 2)
This worksop aims to help you to 
1) use vicenty's functions to compute distance and azimuth (refresh)
3) understand how to create a waypoint given a coord, distance, and azimuth. 
4) create a geodesic traectory given just two waypoints
5) how to plot your waypoints in an external website .

All this could help you to create waypoints in your assignment 

INSTRUCTIONS:
    1.- Place the file "vinc.py" in the same folder as you have placed this file
    2.- Solve it
"""

import vinc # Import an amazing library. 
            # Be rsue that you have placed this file in the same folder
            
# =============================================================================
# # 0.- Observe how the two functions are used.
# ============================================================================= 

boston = (42.3541165, -71.0693514)  #
newyork = (40.7791472, -73.9680804) #
 
distance,azimuth = vinc.v_direct(boston, newyork)  # Meteres, degrees
print(distance)     # meters
print(azimuth)      # degrees

# Define a waypoint
# vinc_in(lat, lon, azimuth, distance ) 

lat2,lon2 = vinc.v_inverse(boston[0],boston[1],azimuth,distance)  
print(lat2,lon2)         # degrees

# =============================================================================
# # 1.- Create a waypoint exactly at the middle of boston and new york.
# ============================================================================= 
print("")
print("EXERCISE 1 BEGINS")
print("")


print("")
print("EXERCISE 1 ENDS")
print("")
# =============================================================================
# # 2.- Create a waypoint exactly at the middle of new york and boston
# #     note that you have to use newyork[0], newyork[1]
# #     Do you think is it going to be the same or different? Why?
# =============================================================================
print("")
print("EXERCISE 2 BEGINS")
print("")


print("")
print("EXERCISE 2 ENDS")
print("")
# =============================================================================
# # 3.- Compute and print the azimuth angle between Boston - Middle waypoint and 
# #     between the middle point and New York. Compute and print the azimuth 
# #     angle between New York - the middle point, and the middle point and 
# #     Boston. What do you expect to see?
# #     What do you observe? Are those azimuth point the same?
# =============================================================================
print("")
print("EXERCISE 3 BEGINS")
print("")


print("")
print("EXERCISE 3 ENDS")
print("")
# =============================================================================
# # 4.- Find the coordinates at Schiphol and create 4 wayponts located  at
# # 200 nautical miles North, East, South and West from the airport. 
# # The distance is 200 nm in a geodesic reference. 
# # Plot the solution in https://www.mapcustomizer.com/
# # Use Bulk entry. (lat,lon)
# # Extra challenge: Try to use two vectors (lists) and a for loop.
# # Vector 1 should contain strings["north","east"...] and vector 2 the 
# # coordinates. Use these two vectors to print the solution inside the for loop.
# =============================================================================
print("")
print("EXERCISE 4 BEGINS")
print("")
# Hint: Use the loaded function and use the azimuth. North is 0 degrees, East 90 degrees and so on.

print("")
print("EXERCISE 4 ENDS")
print("")
# =============================================================================
# # 5.- Create and print 40 equidistant waypoints from LAX to Schiphol. 
# # Print them and plot them in https://www.mapcustomizer.com/
# # mapcustomizer format: lat,lon
# # Extra challenghe: Include the azimuth in a vector. 
# # Extra challenge: Place them in a .txt file as the instructions here:
# # https://www.w3schools.com/python/python_file_write.asp
# =============================================================================
print("")
print("EXERCISE 5")
print("")
 #Hint: First compute the distance between LAX and AMS and divide it by 40

print("")
print("EXERCISE 5 ENDS")
print("")

"""
It is true that mapcustomizer is not the best to be used to plot a graph. 
However, you can do some research online for different tools that can help you
http://dwtkns.com/pointplotter/ is a bit better. 
http://www.hamstermap.com/quickmap.php uses google maps

Another Tutorial on how to create files:
    https://www.guru99.com/reading-and-writing-files-in-python.html

"""
###### END OF WORKSHOP 3 PART 1  ######
