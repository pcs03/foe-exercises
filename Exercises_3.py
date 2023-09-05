# -*- coding: utf-8 -*-
"""
Excercises 3
Version 2: Now a part of the exercises. 
Version 3: Corrected exercise 
FOE 3 - Year 4
@author: Alejandro Murrieta-Mendoza

This script is a refresher of lists and special functions
Please help your colleagues and friends if they need assistance. 

This script is not graded.
The line codes here are just a proposed solution. Youcan implement your own solution 

Objectives:
    1.- Refresh previous basic skills from the last workshops.
    2.- Make your logic using for loops and ifs stronger
    3.- Use pre-defined functions.
    4.- Compute the distance and initial azimuth between two cities <-- Directly 
        related to the assignment
"""
import numpy as np

# 1.- Create a list named my_list with 10 different numeric elements

my_list = np.random.randint(1, 1000, 10)

# 2.- Use a for loop, range(), and len() to print the content of that list

print(f"My list is {len(my_list)} elements long")

for i in my_list:
    print(i)


# 3.- Find and print the maximal value contained in your list. Print the index
#     as well. Print the value from your list using the index.
#     print(list[index]).
#     For this you can use numpy functions "argmax()" and "np.amax()"

max_value = np.amax(my_list)
max_value_index = np.argmax(my_list)

print(
    f"The highest value in the list is {max_value} with and index of {max_value_index}"
)


# 4.- Use a for loop,  methods ".append", and ".size" (this one is a numpy
#     method) to pass the numpy array to a list called my_new_list

a = np.array([1, 2, 3, 4, 5])
my_new_list = []
for i in a:
    my_new_list.append(i)

print(my_new_list)

# 5.- Reverse the content of my_new_list to my_new_inverted_list using for loops.
# Output should be : [5,4,3,2,1]

my_new_inverted_list = [my_new_list[-i - 1] for i in range(len(my_new_list))]

print(my_new_inverted_list)


# 6.- Observe the code below
print("Hello")
print("World!")
print("How is it going?")
# Now look at this
print("Hello", end=" ")
print("World!", end=" ")
print("How is it going?")
# Now look at this
print("Hello", end=" ")
print("World!")
print("How is it going?")
# Do you see what end = ' ' do?
# Python adds a new line after every print() statement.. end = ' ' replaces this
# for anything that we desire. https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/


# 7.- Print the perimeter side of a rectangle. First ask for the side size. Then print
#     the border of the square with that area.
#     Hint: you DO NOT want python to make a new line after each print().
#     * * * * *
#     *       *
#     *       *
#     *       *
#     * * * * *

side = int(input("Input the desired rectangle side size: "))
for i in range(side):
    for j in range(side):
        if i == 0 or i == side - 1 or j == 0 or j == side - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 8.- Print a Triangle. Introduce the base size and make a solid
#     triangle in python. This is the desired output:
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
#     * * * * * *
#     * * * * * * *
#     * * * * * * * *
#     * * * * * * * * *
#     * * * * * * * * * *
#     * * * * * * * * * * *
#     * * * * * * * * * * * *

base = 10
for i in range(base):
    print("* " * (i + 1))

# 9.- Do the same triangle, but instead of typying *, type the number of
#     rows. Base should be beteewn 2 and 9
#     triangle in python. This is the desired output:
#     0
#     1 1
#     2 2 2
#     3 3 3 3
#     4 4 4 4 4
#     5 5 5 5 5 5
#     6 6 6 6 6 6 6
#     7 7 7 7 7 7 7 7

base = 10
for i in range(base):
    print(f"{i} " * (i + 1))

# *** EXERCISES 3 ENDS ***
