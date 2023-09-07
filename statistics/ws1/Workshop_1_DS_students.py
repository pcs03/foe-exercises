#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:06:00 2022

# Explorative Data Analysis Workshop 1  (Statistics for DS)


The instructions in this file assume that you are using Spyder by Anaconda. 
They might be different if you are using Jupyler. For example: Jupyler prints
all columns when you use the command df.head(). Spyder just prints some columns, 
it is desirable to use the Variable Explorer instead. 


# Objective:
    1.- Execute a simple EDA.
    2.- Clean DATA
    3.- Plot Distributions and Box Plots
    4.- Proof that there is a relationship between area and house cost.
    5.- Plot a Categorial Data
    6.- Plot a Correlation Matrix
 
    
@author: Alejandro Murrieta-Mendoza
"""
# 0: Import all your required libreries 
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st

import pandas as pd
import numpy as np

# DATASET PRELIMINAR ANALYSIS
# 1: Load the file "Amsterdam2021.csv" and assign it to df.


# 2: Make a Copy of this dataset to df_original. 
# HINT: DataFrame.copy()


# 3: Explore your dataset. Use the function DataFrame.head() and assign it to data_head.
 

# 3A Open this new variable in the data_head and aswer the next questions

# How many Variables do you have in this dataset?
# How many datapoints do you have in this data set? 
# Use df.shape to verify your answers
# How many continous variables do yo have?
# How many discrete varialbes do you have?
# How many categorial variables do you have in that dataset?

# Discuss your answers with your team member. 
# Use DataFrame.dtypes.astype(str).value_counts() to give you an idea of your answers 
# Do you all agree? Ask another team :)
# Cannot agree? look for me and we can discuss this.

# 4: Print your column names


# 5: Rename "Unnamed: 0" as "Index"



# Now, you have an idea of what information your dataset contains. 

### EDA ###
# EDA: Varibles exporation
# 6.- Save a description of your numerical variables as variable df_description_numerical. 
# HINT: describe()

# 6A.- Observe and analyse the variable df_description_numerical.

# Why is there a difference in the count of datapoints for the variable price?

# Does the information in the variable "index" is useful for the analysis?
# If so, why?. If it is not there why should we or should we not delete it?
# Can we avoid havig that column at all? If you look at the original csv file, 
# that variable does not exist.

# 7.- Save a description of your categorial  variables as variable df_description_categorical.
# HINT: (inclde = object)


# Why are there frequencies of the variable "Address" larger than one? Is this logical?
# Find a frequency of two in your data set and think about it. Example: "Ringdijk, Amsterdam"

# EDA: Missing values
# 8.- Determine how many missing values are in the dataframe
# HINT .isnull() and/or .sum() might help you


# 8A.- Compute the percentage of missing values from the dataset and save it in missing_values_per


# 8B.- Identify and analyse the missing values.
# HINT: isnull() and/or .any(axis =1)
#      What would be the best way to handle these missing values?








# Wait. think about it before going further down
















# Are you sure you gave it enough thought?















# ANTWOORD(yes... a dutch word, Respuesta or Solución sound better, but oh well):
# Remove them for now, they are too different.
# 9.- Remove the values from the data set.
#     HINT: .index and axis = 0 might help.


# 10.- Verify that you indeed delete the N/A values and review the new data point count.
#  HINT: .shape and .isnull().sum()


# 11.- Show a scatter plot for House Price and Area. Name your labels and add
# a title to your plot. 


# Which value is in your Y axis? Why?
# Does it look like a linear relationship to you? 
# In simple words, how would you interpretate this plot?

# 12.- Plot an Histogram for the variable Area. bins= 100. Name your axis 
#      Feel free to play with bins size. What does it do?
#      I expect you to google how to do this... yes i know... just google it...


# 13.- Plot an Histogram for the variable Price. bins= 100. Name your axis


# What can you conclude from this distribution. Are there outliers?
# There are different rules to define outliers. We will cover this in a different
# workshop

# 14.- Draw a Boxplot for House Area. Name your axisa and add a title name
#      Some concepts define an outlier as any point farther from 1.5 IQR. 
#      Under this concept, would you think that there are outliers?

# 15.- Draw a Boxplot for House Price. Name your axis and add a title name
# What is the median for price?


# 16.- Remove the last letters from your ZIP code including the blank space
#      We are coding the ZIP code (witout the letters) to be used as regression 
#      I know... i never told you explicitly how to to this. But you can do it!

# 17.- Change the column ['ZIP] to int
# Hint: .astype(int)


# 18.- Plot the scatter plot Zip Code Vs Price







# Did you expect this result?
# I did not... Why are not houses in Zuid WAAAAY more expensive? Or houses in 
# the center... (i know, who wants to live in the center?... Tourists and AirBNB
# or those expats, expats learn to move out eventually though :)  )

# 19.- Plot the distribution of Zip Code 


# 20.- Plot the distribution of every Zip Code vs Price
# HINT: USE sns.boxplot(x = ____, y = ____)
# Suggestion: _ = plt.xticks(fontsize = 6, rotation=90)
# Would you think there are outliers there?


# 21 - Google the method DataFrame.corr() and implement it 



# What are the two values that postitevly correlate more with Price?
# What is the infleunce of the house location (ZIP code) in Price?

# 22.- Plot a heat correlation map
# HINT: sns.heatmap
# HINT2 : You need corrmat


# Can you undestand this heat map?
# Explain this map to your team memembers.
# Tell them wich variables/features you think are more important and why.
# No one knows? Ask that friend from the other team
# Still lost?
# Come see me

 #### END OF WORKSHOP 1 ####