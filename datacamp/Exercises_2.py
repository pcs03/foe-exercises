#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:46:10 2022
Exercises # 2

Version 2: Problem 6. Value changed from 30250545001 to  3025054999
Objective:
    
    This short set of exercises aims to make you practice basic
    programmning skills
@author: Alejandro Murrieta Mendoza
"""

# 1) :
# Declare two numbers and print:
# a) their sum
# b) their substraction
# c) multiplication
# d) division

x = 5
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)

# 2) :
# Use IF statements to define which number is smaller. Print the value of
# both numbers and print the solution

if x < y:
    print(f"x ({x}) is smaller than y (y{y})")
else:
    print(f"y ({y}) is smaller than x ({x})")

# 3):
# Ask for a number between 0 and 10.
# Define the list (vector)
# numbers = [0,2,4,10]
# define if the provided number is in that listl

input_number = int(input("Input a number between 0 and 10: "))
numbers = [0, 2, 4, 10]

if input_number in numbers:
    print("The input number is in the list")
else:
    print("The input number is not in the list")


# 4):
# Ask for any animal.
# Define the list ( or vector) animals shown below
# animals = ['dog', 'cat', 'fish', 'horse', 'tiger']
# define if the provided animal is in that list

animal = input("Enter an animal: ")
animals = ["dog", "cat", "fish", "horse", "tiger"]

if animal in animals:
    print("The animal is in the list")
else:
    print("The animal is not in the list")

# 5):
# Create a For loop that iterates from 0 to 100 and only print the values
# multiple of 2. Hint: You might want to use modulus (%)

for i in range(0, 101):
    if i % 2 == 0:
        print(i)

# 6):
# Introduce the next equation x^2 + 3x + 1. Set a while loop and evaluate
# the function increasing x per unit per loop (increase x + 1 per loop)
# Example Iteration 1 (x = 0): 0^2 + 3*0 + 1.
# Iteration 2 (x = 1): 1^2 + 3 * 1 + 1,
# Iteration 3 (x = 2): 2^2+ 2*1 + 1, iteration 4 (x = 3): 3^2 + 3*3 + 1....
# the while loop must stop when the solution equals 3025054999
# Print the value of x that provides 3025054999
# The initial value of x must be 0 (iterations begins at 0)

solution = 0
x = 0

while solution != 3025054999:
    solution = x**2 + 3 * x + 1
    x += 1

# 7):
# Create the next vector/list:
# numbers = [10, 3, 6, 9, 12, 66, 103, 43, 14, 125, 4, 1, 0]
# In this vector, 10 is in the position 0, 3 in the position 1 and so on...
# Develop a code that can define:
# 1.- At which position is the value 103?
# 2.- At which position is the value 125?

numbers = [10, 3, 6, 9, 12, 66, 103, 43, 14, 125, 4, 1, 0]


def get_index(list, value):
    return list.index(value)


print(get_index(numbers, 103))
print(get_index(numbers, 125))

# 8):
# With the same vector/list numbers, using the form:  print(numbers[x])
# print the numbers 10, 66, 14, and 0.

print(numbers[get_index(numbers, 10)])
print(numbers[get_index(numbers, 66)])
print(numbers[get_index(numbers, 14)])
print(numbers[get_index(numbers, 0)])


# **** Excercises 2 Ends ****
