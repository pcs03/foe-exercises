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

def leapyear(year):
    if year%400 ==0:
        yes_no = 1
    elif year%100 ==0:
        yes_no = 1
    elif year%4 == 0:
        yes_no = 1
    else:
        yes_no = 0
    return yes_no

def num_days(days, months, years, leap):
    total_days = 0
    if years[0] == years[1]:
        stop = 0
        if months[0] == months[1]:
            total_days = days[1] - days[0] + 1
        else: 
           for i in range (months[0], months[1]):
               total_days += days_months(i)
               total_days = total_days - days[0] - (days_months(months[1])- days[1])
    elif years[1] > years[0]:
        current_month = days_months(months[0]) - days[0] + 1
        if months[0] <= 2:
            extra_day = leapyear(years[0])
        else:
            extra_day = 0

        total_days =  current_month + extra_day
        for i in range(months[0]+1, 13):
            total_days += days_months(i)
        
        
        # CURRENT YEAR IS DONE
        
        # Last Year:
        last_month = days[1]
        if months[1] > 2:
            extra_day = leapyear(years[1])
        else:
            extra_day = 0
            
        for i in range(1, months[1]):
            total_days += days_months(i)
            
        total_days = total_days + last_month
        
        
        # The rest of the years
        
        total_leapyear = 0
        for i in range (years[0]+1,years[1]+1):
            total_leapyear += leapyear(i)
            
        days_in_years = (years[1]- years[0] - 1)*365+total_leapyear
        
        total_days = total_days + days_in_years - 1 #Excluding current day
    return total_days;

def num_hours (days):
    return days*24

def num_seconds (hours):
    return hours * 60

def print_all(days, hours, seconds):
    print("There are " + str(days) + " days")
    print(str(hours) + " hours")
    print(str(seconds) + " seconds")
    return

def days_months(month):
    switcher = {
        1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,
        }
    return switcher.get(month, "ERROR")

date_1_day = 30
date_1_month = 7
date_1_year = 2001

date_2_day = 27
date_2_month = 10
date_2_year = 2022

# STEP 1: Create a function that computes the number of days between two dates
# STEP 2: Create a function that computes the number of minutes between two dates
# STEP 3: Create a function that computes the number of hours between two dates
# STEP 4: Create a function taht prints the number of days, minutes, and hours
#         between two dates. 

# STEP 4: Ask for two dates
# STEP 5: Print the required inforamtion 

year_1_leap = leapyear(date_1_year)
year_2_leap = leapyear(date_2_year)

days = num_days([date_1_day,date_2_day],
                [date_1_month,date_2_month],
                [date_1_year,date_2_year],
                [year_1_leap,year_2_leap])
hours = num_hours(days)

seconds = num_seconds(hours)

print("Between the " + str(date_1_day) + "/" +str(date_1_month)+'/' + str(date_1_year))
print("And the ")
print(str(date_2_day) + "/" +str(date_2_month)+'/' + str(date_2_year))
print_all(days, hours, seconds)
