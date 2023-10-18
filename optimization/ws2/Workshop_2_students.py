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

    NO UNITS (Wind Factor)

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
import qty
from matplotlib.cbook import Stack
from vinc import v_direct, v_inverse

"""
2.- Load the data shown in the introduction  (the 9 lists above)
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


class Coord:
    def __init__(self, lat: float, lon: float):
        self._lat = lat
        self._lon = lon

    @property
    def latlon(self) -> tuple[float, float]:
        return (self._lat, self._lon)

    @property
    def lat(self) -> float:
        return self._lat

    @property
    def lon(self) -> float:
        return self._lon

    def __str__(self):
        return f"{self._lat}° {'N' if self._lat >= 0 else 'S'}, {self._lon}° {'E' if self._lon >= 0 else 'W'}"


start_coord = Coord(lat_lef[0], lon_lef[0])
end_coord = Coord(lat_lef[-1], lon_lef[-1])

left_df: list[float] = [(lefDF[i] + lefDF[i + 1]) / 2 for i in range(len(lefDF) - 1)]
mid_df: list[float] = [(midDF[i] + midDF[i + 1]) / 2 for i in range(len(midDF) - 1)]
right_df: list[float] = [(rigDF[i] + rigDF[i + 1]) / 2 for i in range(len(rigDF) - 1)]

left: list[Coord] = [Coord(lat, lon) for (lat, lon) in zip(lat_lef, lon_lef)]
mid: list[Coord] = [Coord(lat, lon) for (lat, lon) in zip(lat_mid, lon_mid)]
right: list[Coord] = [Coord(lat, lon) for (lat, lon) in zip(lat_rig, lon_rig)]

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

dist_left, dist_mid, dist_right = 0, 0, 0

for i in range(1, len(left)):
    dist_left += v_direct((left[i - 1].lon, left[1 - 1].lat), (left[i].lon, left[i].lat))[0] * left_df[i - 1]
    dist_mid += v_direct((mid[i - 1].lon, mid[1 - 1].lat), (mid[i].lon, mid[i].lat))[0] * mid_df[i - 1]
    dist_right += v_direct((right[i - 1].lon, right[1 - 1].lat), (right[i].lon, right[i].lat))[0] * right_df[i - 1]

print(f"Left: {qty.Distance(dist_left).km} km, {qty.Distance(dist_left).n_mile} NM")
print(f"Mid: {qty.Distance(dist_mid).km} km, {qty.Distance(dist_mid).n_mile} NM")
print(f"Right: {qty.Distance(dist_right).km} km, {qty.Distance(dist_right).n_mile} NM")

"""
4.- In this step, a simple greedy optimization method should be applied.
    Try to optimize your distance by calculating at each waypoint, the
    shortest path. The aircraft should calculate the costs of going to either
    one of the options (left, middle or right), and fly to the least expensive.
    This process should be repeated until the aircraft reaches the last waypoint.
    Show this trajectory on the map (or a scatter plot). You can move along mid, left or right. 
    Be sure to show witha different color the points where the "optimal" candiate is located
"""


def heuristic(coord: Coord) -> float:
    dist_to_dest = v_direct(coord.lon, coord.lat)[0]
    return dist_to_dest


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def emtpy(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


# class GreedyFrontier(StackFrontier):
#     def remove(self):


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
