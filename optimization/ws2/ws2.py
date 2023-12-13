# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:48:53 2019

@ Adaptaed to Python by Alejandro Murrieta-Mendoza

INTRODUCTION:
    
In this workshop, you will optimize a flight trajectory using two different
methods. First, analyze the following code for three different trajectories
(left, middle and right). You can also find distance factors, which are
randomized factors that simulates the effect of the wind on the aircraft's speed. 
For example, a distance factor of 1.1 would mean that the distance between 
point A and point B is increased by 10%, simulating headwind. 
A distance factor of 0.9 simulates tailwinds thus the distance is reduced. 


This is your DATA (See Figure 2 in DLO to understand this):
    ALL IN DEGREES
lon_lef = [4.76, 4.87, 3.69, 2.36, 2.74, 2.88, 2.69]
lat_lef = [52.30, 52.05, 50.31, 48.41, 46.09, 43.82, 41.88]
lon_mid = [4.76, 4.79, 3.62, 2.287, 2.67, 2.81, 2.69]
lat_mid = [52.30, 52.04, 50.30, 48.39, 46.09, 43.81, 41.88]
lon_rig = [4.76, 4.72, 3.55, 2.21, 2.59, 2.73, 2.69]
lat_rig = [52.30, 52.04, 50.30, 48.39, 46.09, 43.81, 41.88]

    NO UNITS (Wind Factor)
midDF = [1.1, 1.2, 1, 0.96, 0.99, 0.98, 0.95]
lefDF = [1.1, 0.95, 0.96, 0.99, 1.2, 1.2, 0.95]
rigDF = [1.1, 0.9, 0.97, 1, 1.2, 1.2, 0.95]

lon_mid and lat_mid are the coordinates for the reference trajectory
lon_rig and lat rit are the coordinates for the trajectory at the right
midDF, leftDF, and rig DF are the distance factores (wind emulation)




"""

"""
1.- Place the vinc.py file (workshop 1 - optimization) in the same directory as this file. 
Then load the v_direct and v_inverse functions. 
"""

from avipy import geo, qty

"""
2.- load the data shown in the introduction  (the 9 lists above)
"""
lon_lef = [4.76, 4.87, 3.69, 2.36, 2.74, 2.88, 2.69]
lat_lef = [52.30, 52.05, 50.31, 48.41, 46.09, 43.82, 41.88]
lon_mid = [4.76, 4.79, 3.62, 2.287, 2.67, 2.81, 2.69]
lat_mid = [52.30, 52.04, 50.30, 48.39, 46.09, 43.81, 41.88]
lon_rig = [4.76, 4.72, 3.55, 2.21, 2.59, 2.73, 2.69]
lat_rig = [52.30, 52.04, 50.30, 48.39, 46.09, 43.81, 41.88]

midDF = [1.1, 1.2, 1, 0.96, 0.99, 0.98, 0.95]
lefDF = [1.1, 0.95, 0.96, 0.99, 1.2, 1.2, 0.95]
rigDF = [1.1, 0.9, 0.97, 1, 1.2, 1.2, 0.95]

"""
3.- Using a For loop, calculate the total distance, including the distance
    factors, for each one of the trajectories. Use the average of distance
    factors between point A and point B. Example, if the aircraft is at the
    first waypoint of the middle trajectory, and it flies to the second
    waypoint of the middle trajectory, the distance factor to be used
    would be (1.1+1.2)/2 (see data above). 
    Which one is the shortest trajectory?
    Print the result in km and in nautical miles

"""
left_path = 0
mid_path = 0
right_path = 0

for i in range(len(lon_lef) - 1):
    left_coord = geo.Coord(lat_lef[i], lon_lef[i])
    mid_coord = geo.Coord(lat_mid[i], lon_mid[i])
    right_coord = geo.Coord(lat_rig[i], lon_rig[i])

    left_wf = (lefDF[i] + lefDF[i + 1]) / 2
    mid_wf = (midDF[i] + midDF[i + 1]) / 2
    right_wf = (rigDF[i] + rigDF[i + 1]) / 2
    
    left_path += left_coord.get_distance_bearing(geo.Coord(lat_lef[i + 1], lon_lef[i + 1]))[0] * left_wf
    mid_path += mid_coord.get_distance_bearing(geo.Coord(lat_mid[i + 1], lon_mid[i + 1]))[0] * mid_wf
    right_path += right_coord.get_distance_bearing(geo.Coord(lat_rig[i + 1], lon_rig[i + 1]))[0] * right_wf

print(f"Left path: {left_path}")
print(f"Mid path: {mid_path}")
print(f"Right path: {right_path}")

"""
4.- In this step, a simple greedy optimization method should be applied.
    Try to optimize your distance by calculating at each waypoint, the
    shortest path. The aircraft should calculate the costs of going to either
    one of the options (left, middle or right), and fly to the least expensive.
    This process should be repeated until the aircraft reaches the last waypoint.
    Show this trajectory on the map (or a scatter plot). You can move along mid, left or right. 
    Be sure to show witha different color the points where the "optimal" candiate is located.
    Use the wind factor.
"""

# List of the path, with the starting coordinate
path: list[tuple[str, geo.Coord]] = [("mid", geo.Coord(lat_mid[0], lon_mid[0]))] 

for i in range(len(lon_lef) - 1):
    current_node = path[-1]
    current_path = current_node[0]
    current_coord = current_node[1]

    if current_path == "left":
        left_wf = (lefDF[i] + lefDF[i + 1]) / 2
        mid_df = (lefDF[i] + midDF[i + 1]) / 2
        left_wf = (lefDF[i] + rigDF[i + 1]) / 2


    left_coord = geo.Coord(lat_lef[i], lon_lef[i])
    mid_coord = geo.Coord(lat_mid[i], lon_mid[i])
    right_coord = geo.Coord(lat_rig[i], lon_rig[i])

    left_wf = (lefDF[i] + lefDF[i + 1]) / 2
    mid_wf = (midDF[i] + midDF[i + 1]) / 2
    right_wf = (rigDF[i] + rigDF[i + 1]) / 2
    
    left_path += left_coord.get_distance_bearing(geo.Coord(lat_lef[i + 1], lon_lef[i + 1]))[0] * left_wf
    mid_path += mid_coord.get_distance_bearing(geo.Coord(lat_mid[i + 1], lon_mid[i + 1]))[0] * mid_wf
    right_path += right_coord.get_distance_bearing(geo.Coord(lat_rig[i + 1], lon_rig[i + 1]))[0] * right_wf

print(f"Left path: {left_path}")





"""
5.- In this step, a simple greedy optimization with a simple heuristic should be
    applied. Try to optimize your distance by calculating the shortest path
    at each waypoint, . The aircraft should calculate the costs of going to either
    one of the options (left, middle or right). Besides calculating the shortest
    immediate path, you should also calculate the distance from the current pont to 
    the final waypoint to try to avoid local optimum. 
    Does this method improves the previous result?
    Why?
"""
# CODE


# 6.- Open the Figure_1.png from Brigthspace. You are traveling from point A to point Z. 
#     1.- Create an adjacent matrix showing the connections between different nodes.
#         Think about how that adjacent matrix will be used. How does the algorithm know where
#         "to go" next.
#     Hint: You can rename your points to make it easier to make it easier to identify and 
#            visualize in your adjancent matrix. 


### WORKSHOP ENDS ####
