#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 15:19:54 2022
This script provides an example of how to load the weather data and how to 
access the closest point to the provided data

Version 2:
    The line to obtain the longitudal index was fixed to actually obtain the
    correct values if flying from 0 - 180E. 
    
Version 3:
    row selection for negative values has been fixed. 
@author: Alejandro Murrieta-Mendoza
"""

import numpy as np


def load_weather():
    TMP = np.genfromtxt("TMP_date_1_alt_1.csv", delimiter=",")
    WIND = np.genfromtxt("WIND_date_1_alt_1.csv", delimiter=",")
    WDIR = np.genfromtxt("WDIR_date_1_alt_1.csv", delimiter=",")
    return TMP, WIND, WDIR


tmp, wind, wdir = load_weather()

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

lat = 51.5083
lon = -0.12574

# if lat > 0:
lat = lat + 90  # real coordinate
lat_i = lat / 180
lat_i = lat_i * 301
lat_i = round(lat_i)  # index


lon = 180 + lon

lon_i = lon / 360
lon_i = lon_i * 601
lon_i = round(lon_i)  # index

# The operation at row provides the row where the desired indeces are located
row = (lat_i - 1) * 601 + lon_i - 1

print("The required indeces are: ")
print("For i index (lon_i) :  " + str(lon_i))
print("For j index (lat_i) :  " + str(lat_i))

print("The approximateive coordinate are: ")
print("Longitude :  " + str(lon_i * 0.6))  # 0.6 as it is the separation
print("Latitude :  " + str(lat_i * 0.6))
print("")

temperature_row = tmp[row]
temperature = tmp[row][2]
print("The temperature row " + str(row) + " contains the following information:")
print(temperature_row)
print("")

wind_speed_row = wind[row]
wind_speed = wind[row][2]

print("The wind row " + str(row) + " contains the following information:")
print(wind_speed_row)
print("")

wind_dir_row = wdir[row]
wind_dir = wdir[row][2]

print("The wind dir row " + str(row) + " contains the following information:")
print(wind_dir_row)
print("")

"""
    Run the script.
    The results show that the row variable provide the required indices. 
    The temperature at the closest point to (51.5083,-0.12574)
    is 231.077 Kelvin, the wind speed is  6.0342 knots and 
    the wind angle is 249.5 degrees.
    
    The coordiantes for the closest point are (142.2, 180)
    or: (142 - 90, 180-180)
        (52 N, 0 W) 
"""
