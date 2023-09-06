#!/usr/bin/env python3
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


from dataclasses import dataclass

month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_lengths_leap = [29 if num == 28 else num for num in month_lengths]


@dataclass
class Date:
    year: int
    month: int
    day: int
    hour: int
    minute: int


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


date1 = Date(2023, 1, 1, 0, 0)
date2 = Date(2023, 1, 10, 0, 0)

print(date1)

print(is_leap_year(13096))


# STEP 1: Create a function that computes the number of days between two dates
# STEP 2: Create a function that computes the number of minutes between two dates
# STEP 3: Create a function that computes the number of hours between two dates
# STEP 4: Create a function taht prints the number of days, minutes, and hours
#         between two dates.

# STEP 4: Ask for two dates
# STEP 5: Print the required inforamtion
