#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 2022
Exercices # 1
Objective:
    
    This script contains a series of simple exercises to help you practice
    the different initial concepts
    
@author: Alejandro Murrieta-Mendooza
"""

# 1.- Declare two variables x = 7 and y = 5

x = 7
y = 5

# 2.- Print y+x, y*x, y/w, y**x, and y%2.
#    What does y**x and y%2 do?

print(y + x)
print(y * x)
print(y / x)
print(y**x)  # y to the power of x
print(y % 2)  # remainder of y / 2. 1 in this case

# 3.- Create a List with the numbers from 0 to 10.

range_list = list(range(0, 11))

# 4.- Using a for loop, print each element in the list

for element in range_list:
    print(f"list element: {element}")

# 5.- Print the value of the 3rd value of your list plus the 8th value of your
#     list.

print(f"Sum of 3rd element and 8th element: {range_list[2] + range_list[7]}")

# 6.- Define x = 3 and y = 7, and ask for a number z = 10. Using IF statements,
#     define which one is the largest one.

x = 3
y = 7
z = int(input("Input an integer for the variable z: "))

if z > max(x, y):
    print(f"z ({z}) is the highest number")
elif y > max(x, z):
    print(f"y ({y}) is the highest number")
else:
    print(f"x ({x}) is the highest number")

# 7.- Extract each digit from an integer in the reverse order.
#     Example, given x  = 1234, x should be x = 4321

from random import randrange

integer = randrange(12000)

print(f"For the integer '{integer}', the reverse is '{str(integer)[::-1]}'")

# 8.- Write a function called addition(x, y) that returns the sum of two numbers.


def addition(x, y):
    return x + y


# 9.- Put your name in a variable
#    a.- print all letters as capital letters
#    b.- print all leters in lower scape
#    c.- Ask for a name
#    d.- Only print the variable name if the answer is correct (your name)

name = "Paolo"
print(name.upper())
print(name.lower())

input_name = input("Input your name: ")
if input_name.lower() == name.lower():
    print(name)

# 10.- Write a program to iterate from 0 to 15 and in each iteration, print
#    the sum of the current and previous number (Use For or While).
#    The first iteration (for 0), the output must be 0.

for i in range(0, 16):
    print(i + i - 1 if i != 0 else 0)

# 11.- Write a program to iterate the first 15 numbers and in each iteration,
#    print the sum of the current and next number (Use For or While)

for i in range(0, 16):
    print(i + i + 1)

# 12.- Write a function that converts the input (Farenhaits) to Celcius and
#      print the result.


def f_to_c(temp_f):
    return 5 / 9 * (temp_f - 32)


print(f_to_c(-40))
# ***** Excercises 1 Ends *****
