#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:06:00 2022

# Explorative Data Analysis Workship 1


The instructions in this file assume that you are using Spyder by Anaconda. 
They might be different if you are using Juypler. For example: Jupyler prints
all columns when you use the command df.head(). Syder just prints some columns, 
and it is desirable to use the Variable Explorer instead. 


# Objective:
    1.- Develop a regression algorithm
    2.- Plot residuals and verify distribution.
    3.- Obtain the R-Squared values
    4.- Analyse Influencial Waypoints
    5.- Cook's Distance
    6.- Predict Values
    
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


# 1: Load the file "Amsterdam2021.csv"  as a dataframe
#    This dataset was obtained from Pararius


# 2: Make a Copy of this dataset to df_original.


# 3: Explore the dataset, clean the n/a values and rename column 0 to 'Index'



# 4: There are many ways to develop a regression model in python. For this 
#    workhops, we will be using the library statsmodel. Please read the
#    documentation at: https://www.statsmodels.org/stable/regression.html
#    You should ulse OLS.
 # Define vector y:


 # Define vector x:


 # If needed: add constant to variables

     
 # Develop model

 
# 5: Print the model summary. Look for method .summary()


# 6: use the class .params to obtain B0 and B1.

# What is the constant value B0?

# What is your slope B1?

# Write your equation in a piece of paper. 


# 7.- Use the seaborn function to plot the datapoints, the regression line, 
#     but do not plot the confidence shade. Documentation:
#     https://seaborn.pydata.org/generated/seaborn.lmplot.html
#     - The line color should be different than the datapoints.
#     - The regression line should not be truncated 


# From this plot: 
#    How many outliers can you detect?
#    By inspection. What point has the largest residual?
#    Are there any points with high leverage?
#    Do you think that data point in around x = 640 is an influencial datapoint?
#    What point do you think has the most influence?
#    Are all these points the same?

# 8.- Obtain the residuals using the class resid and determine the largest
#     residual and its index. Print its information from the dataframe
#     Largest can be in any direction : Positive or Negative



# Does it match the one you guessed in the previous question?

# 9.- Plot the residuals using sns.residplot



# Looking at the residuals... What is the value with the most influence according
# to you?

# Are the residuals normally distributed?

# 10.- Compute the mean of your values in Area and plot a line in there


# Does it help you to estimate the most influence values?

# 11.- Explore the classes MODEL_NAME.get_influence(), and  
#      MODEL_NAME.get_influence().summary_frame()

# Assign YOUR_MODEL_NAME.get_influence() to variable model_influence


# Assign YOUR_MODEL_NAME.get_influence().summary_frame() to model_influence_summary


# If you explore the variable model_influence, there are many different 
# methods that can be used to obtain different information. One of those 
# methods is indeed ".summary_frame()". Feel free to explore them. 


# What information does .get_influence().summary_frame() provide? Do you recognize
# some of the columns names?

# Google the other colummns names. They were not covered in the workshop 
# slides, but they are interesting to know for regression analysis. 
# Leverage is called "hat_diag"


# 12.- Plot your leverage in a way where you think you can properly visualize it




# Compare this against your scatter plot. Does it makes sense? 


# 13.- Save the Cook's Distance in a variable and plot it


# What do you think now? Are there any points that surprise you? 
# Can you guess from your scatter plot which points are those?

# 14.- Sort your points in an ascending order and observe the values


# 15.- Pick a cut off method and filter the influential points.  


# 16.- Save the information of your affected points in influential_data_points


# Look at them

# 17.- Plot influential_data_points in a new scatter plot (You might want 
#      to add the regression line)


# 18.- Double click in your model variable name in your variable explorer. 
#      You can see that there are many methods and many "constants" from your
#      model. One of these values is the r-squared value. Localize it and
#      save it in model_1_r


# 19.- Remove one influential data point at each time and develop a new model.
#      The other inlfuential points should be kept. And:
#      A.- Obtain the interceptor and the coefficient
#      B.- Plot the New regression line with an scatter plot
#      C.- Plot the removed point as an X
#      D.- Obtain the new r_squared


    
 
# Does the line changes too much in these examples?
# What is the R squared value?
# Is there a relationship on the influenatial datapoints and the r-squared ?

# 20. Remove all the influential Data points. 
#   A.- Develop the new model
#   B.- Plot the regression line
#   C.- Show the R-Squared value

# Drop values


# Create New Model




# After doing all this work. What do you think is the best way to deal with 
# these points?

# It is always a good idea to analyse your influence values. Sometimes they
# will have an important effect on your models. Other times they will not. 
# you must always verify this before removing them. 


# 21. Use the original model coefficients to predict the house price for:
#   A.- 44 m^2
#   A.- 100 m^2
#   B.- 250 m^2
#   C.- 400 m^2
#   D.- 550 m^2
#   E.- All of these values at the same time
# B0 = 
# B1 = 


# If you loooked at funda.nl back in 2021, you will find out that these prices
# are waaaaay too low :)