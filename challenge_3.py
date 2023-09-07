#!/usr/bin/ python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6  2022

Challenge 3 
Problem
Ask for two different dates. Using three different functions compute: 
    1) The number of days between the two dates.
    2) The number of hours betwen the two dates.
    3) The number of seconds between the two dates. 

Take into account the days at each month. 
Take into account leap years. 
Do not take into account summer or winter times (+/- 1 hour)
Objective: 
    1.- Use of functions

"""

import math
from datetime import datetime, timedelta


def get_sec_delta(date1: datetime, date2: datetime) -> int:
    delta_sec = date2.timestamp() - date1.timestamp()
    return delta_sec


def get_min_delta(date1: datetime, date2: datetime) -> int:
    delta_min = get_sec_delta(date1, date2) / 60
    return delta_min


def get_hour_delta(date1: datetime, date2: datetime) -> int:
    delta_hour = get_sec_delta(date1, date2) / 3600
    return delta_hour


def get_day_delta(date1: datetime, date2: datetime) -> int:
    delta_days = get_sec_delta(date1, date2) / (3600 * 24)
    return delta_days


def print_delta(date1: datetime, date2: datetime) -> None:
    delta_days = math.floor(get_day_delta(date1, date2))
    delta_hour = math.floor(get_hour_delta(date1, date2))
    delta_min = math.floor(get_min_delta(date1, date2))

    print(f"between {date1} and {date2}, there are {delta_days} days, {delta_hour} hours and {delta_min} minutes.")


if __name__ == "__main__":
    date1 = input("Please enter a comma separated list of values for the first date (year, month, day): ")
    date1 = datetime(*(int(x) for x in date1.split(",")))
    date2 = input("Please enter a comma separated list of values for the second date (year, month, day): ")
    date2 = datetime(*(int(x) for x in date2.split(",")))

    print_delta(date1, date2)

# STEP 1: Create a function that computes the number of days between two dates
# STEP 2: Create a function that computes the number of minutes between two dates
# STEP 3: Create a function that computes the number of hours between two dates
# STEP 4: Create a function taht prints the number of days, minutes, and hours
#         between two dates.

# STEP 4: Ask for two dates
# STEP 5: Print the required inforamtion


# print_delta(datetime(2000, 1, 1), datetime(2008, 3, 3))
# print_delta(datetime(2000, 3, 3), datetime(2008, 3, 3))
# print_delta(datetime(2000, 3, 3), datetime(2022, 10, 27))
# print_delta(datetime(1999, 8, 8), datetime(2022, 10, 27))
# print_delta(datetime(1999, 6, 8), datetime(2022, 10, 27))
# print_delta(datetime(2001, 7, 30), datetime(2022, 10, 27))
