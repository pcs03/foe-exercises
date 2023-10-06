#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:34:00 2022

# Worksho 3: Multivariable Regression


The instructions in this file assume that you are using Spyder by Anaconda. 
They might be different if you are using Juypler. For example: Jupyler prints
all columns when you use the command df.head(). Syder just prints some columns, 
and it is desirable to use the Variable Explorer instead. 


# Objective:
    1.- Explore cocnepts such as Transformation and scaling.
    2.- Create a multivariable model.
    3.- Observe standarized residuals. 
 


@author: Alejandro Murrieta-Mendoza
"""
# 0: Import all your required libreries 
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from sklearn.preprocessing import StandardScaler
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st

import pandas as pd
import numpy as np


# 1: Load the file "Amsterdam2021.csv"


# 2: Make a Copy of this dataset to df_original.


# 3: Clean the data set as in the last workshop



# 4: Develop a linear regression model as in the last workshop. 
 # Define vector y as Price


 # Define vector x as Area


 # Add the constant to x

     
 # Develop model


 
# 5: Save the parameters B0, B1,and rsquared to be compared later


# 6.- Plot your regression line along with the datapoints by using sns.lmplot


# 7.- Create a dataframe with Area and price only and assign it to df_scaled_org


# 8.- Standarized your values using MinMaxScaler and df_scaled_org.
#     Assing your scaled values to df_scaled
#     Compare df_scaled_org and df_scaled


# 9.- Plot your scaled data along with its regression line using sns.lmplot


# Does your data chaged?

# In this particular dataset, the regression line is not affected. However, it is
# always a good idea to verify the influence in your model.

 


# 10. Assign your dataframe df_scaled_org to df_scaled_norm and normalize it

# 11.- Using sns.displot(), plot an histogram with your original 


# 12.- Transform your data in x using np.log() and assign it to x_log.
#      Using sns.displot(), show the new distribution. 


# Is the data "more" normally distributed?

# 13.- Now let's create a multivariable regression model. Include the feature 
#      rooms to your analysis. 

# Create variables y as price and convert it to a np.array


# Create variables x as Are and convert it to a np.array


# Crate variable z as Room and convert it to np.array



# Concatenate x anx z in a single variable
# Explore the command np.c_[]


# Fit your model using sm.OLS as done in previous workshops
# HINT: x is now an array with many columns 


# 14.- Print the interceptor value along with B1 and B2
#      Also print the r^2 value and the r^2 adjusted
# Hint: .params[]





# What is the best r^2 to use for this model? Why?

# 15.- Form your equation and predict the price of a 50 m^2 house with 2 rooms 



# Can you make predictions for a 44 m^2 and 0 rooms?
# Why?

# 16.- Observe the studiantized residuals with outlier_test()
# The colummns name are [student_resid, unadj_p, bonf(p)]


# Find the residuals candidate for outliers. 


#17.- Obtain the studiantized resudials from the original model in quesiton 5


# Obtain the candidate values for outliers


# 18.- Remove first the point with the highest value and recreate the model. 


# Observe the results. Does the model change? 


#### This ends the workshop for statistics for Data Science
# The goal of this set of workshops was to guide you in the implementation of 
# a simple model and observe different techniques to detect outliers.
# One of the most important things missing in these workshops was the creation
# of dummy variables for categorial features. It is for you to invetigate this.
# 
# It is also important to remind you that you can use any algorithm that you
# like. Lienear regresssion was only used as an example to show concepts. 
# The data for your assignment will be uploaded shortly. 
# Good  Luck!
# END OF WORKSHOPS