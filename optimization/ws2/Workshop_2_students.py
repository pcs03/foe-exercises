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
from math import dist

import pandas as pd
from vinc import v_direct, v_inverse

"""
2.- Load the data shown in the introduction  (the 9 lists above)
"""

df = pd.DataFrame(
    {
        "lon_left": [4.76, 4.87, 3.69, 2.36, 2.74, 2.88, 2.69],
        "lat_left": [52.30, 52.05, 50.31, 48.41, 46.09, 43.82, 41.88],
        "lon_mid": [4.76, 4.79, 3.62, 2.287, 2.67, 2.81, 2.69],
        "lat_mid": [52.30, 52.04, 50.30, 48.39, 46.09, 43.81, 41.88],
        "lon_right": [4.76, 4.72, 3.55, 2.21, 2.59, 2.73, 2.69],
        "lat_right": [52.30, 52.04, 50.30, 48.39, 46.09, 43.81, 41.88],
        "df_left": [1.1, 0.95, 0.96, 0.99, 1.2, 1.2, 0.95],
        "df_mid": [1.1, 1.2, 1, 0.96, 0.99, 0.98, 0.95],
        "df_right": [1.1, 0.9, 0.97, 1, 1.2, 1.2, 0.95],
    }
)

print(df)


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

dist_left = []
dist_mid = []
dist_right = []


def get_segment_distances(df: pd.DataFrame, track: str):
    distances = []
    for i in range(df.shape[0] - 1):
        lon_left1, lat_left1, lon_mid1, lat_mid1, lon_right1, lat_right1, df_left1, df_mid1, df_right1 = df.iloc[[i]][
            [["lon_left", "lat_left", "lon_mid", "lat_mid", "lon_right", "lat_right", "df_left", "df_mid", "df_right"]]
        ].values[0]

        lon_left2, lat_left2, lon_mid2, lat_mid2, lon_right2, lat_right2, df_left2, df_mid2, df_right2 = df.iloc[
            [i + 1]
        ][
            [["lon_left", "lat_left", "lon_mid", "lat_mid", "lon_right", "lat_right", "df_left", "df_mid", "df_right"]]
        ].values[
            0
        ]

        df_left = (df_left1 + df_left2) / 2
        df_mid = (df_mid1 + df_mid2) / 2
        df_right = (df_right1 + df_right2) / 2

        dist_left = v_direct((lat_left1, lon_left1), (lat_left2, lon_left2))
        dist_mid = v_direct((lat_mid1, lon_mid1), (lat_mid2, lon_mid2))
        dist_right = v_direct((lat_right1, lon_right1), (lat_right2, lon_right2))

        print(dist_left, dist_mid, dist_right)

    distances.append(0)
    return distances


df["dist_left"] = get_segment_distances(df, "left")
df["dist_mid"] = get_segment_distances(df, "mid")
df["dist_right"] = get_segment_distances(df, "right")

print(df[["dist_left", "dist_mid", "dist_right"]].sum() / 1000)
"""
4.- In this step, a simple greedy optimization method should be applied.
    Try to optimize your distance by calculating at each waypoint, the
    shortest path. The aircraft should calculate the costs of going to either
    one of the options (left, middle or right), and fly to the least expensive.
    This process should be repeated until the aircraft reaches the last waypoint.
    Show this trajectory on the map (or a scatter plot). You can move along mid, left or right. 
    Be sure to show witha different color the points where the "optimal" candiate is located
"""
# CODE


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

### WORKSHOP ENDS ####
