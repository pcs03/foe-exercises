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

from avipy import geo, qty

# =============================================================================
# # 0.- Observe how the two functions are used.
# =============================================================================

boston = geo.Coord(42.3541165, -71.0693514)
newyork = geo.Coord(40.7791472, -73.9680804)

print("Boston: ", boston)
print("NYC: ", newyork)

distance, azimuth = boston.get_distance_bearing(newyork, method="vincenty")
print(f"{azimuth=}")
print(f"{distance.base=}")

coord2 = boston.get_next_coord(distance, azimuth, method="vincenty")
print(coord2)

# =============================================================================
# # 1.- Create a waypoint exactly at the middle of boston and new york.
# =============================================================================
print("")
print("EXERCISE 1 BEGINS")
print("")

coord_middle = boston.get_next_coord(distance / 2, azimuth)
print(coord_middle)

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

_, azimuth_ny_boston = newyork.get_distance_bearing(boston)
coord_middle2 = newyork.get_next_coord(distance / 2, azimuth_ny_boston)
print(coord_middle2)

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

_, azi1 = boston.get_distance_bearing(coord_middle)
_, azi2 = coord_middle2.get_distance_bearing(newyork)
print("Boston - Middle: ", azi1)
print("Middle - NYC: ", azi2)

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

eham = geo.Coord(52.308056, 4.764167)

coords = {}
for i in range(0, 360, 90):
    coords[i] = eham.get_next_coord(qty.Distance.N_mile(200).base, i).get_latlon()

for azi, coord in coords.items():
    print(f"Azimuth: {azi} | Lat: {coord[0]}, Lon: {coord[1]}")

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
# Hint: First compute the distance between LAX and AMS and divide it by 40
lax = geo.Coord(33.942791, -118.410042)
eham = geo.Coord(52.308056, 4.764167)

print(lax)
print()

dist, azi = eham.get_distance_bearing(lax, method="vincenty")
dist_part = dist / 40

coords = [eham]
azimuths = []

for i in range(40):
    _, azi = coords[-1].get_distance_bearing(lax, method="vincenty")
    next_coord = coords[-1].get_next_coord(qty.Distance(dist_part), azi, method="vincenty")
    coords.append(next_coord)
    azimuths.append(azi)

azimuths.append(-1)

for azi, coord in zip(azimuths, coords):
    print(azi, coord)

print(f"Number of coordinates: {len(coords)}. EHAM + KLAX + 40 intermediate waypoints")


print("")
print("EXERCISE 5 ENDS")
print("")

"""
It is true that mapcustomizer is not the best to be used to plot a graph. 
However, you can do some research online for different tools that can help you
http://dwtkns.com/pointplotter/ is a bit better. 
http://www.hamstermap.com/quickmap.php uses google maps

Do you have any suggestion how to easily plot in a map?
Please contact Alex to add this for future workshops. 

Another Tutorial on how to create files:
    https://www.guru99.com/reading-and-writing-files-in-python.html

"""
###### END OF WORKSHOP 3 PART 1  ######
