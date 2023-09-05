#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
challenge 1:
    
Created on Wed Jul  6 2022
Problem
Ask a given integer number to the user. The given number should then be translated
to Morse code. Separate the numbers by two spaces. The program keeps requesting
numbers until the user types "quit" (removing the quotes). The program should 
validate the input. Only Integer numbers, decimal numbers and the word "quit" 
should be valid. 

Some Steps to guide you are shown below. However they are not complete. These
steps are just a proposal, you can do whatever you see fit. 


Morse Code:
0    -----
1    ..---
2    ..---
3    ...--
4    ....-
5    .....
6    -....
7    --...
8    ---..
9    ----.
.    .-.-.-

Objective: 
    1.- Use a while loop
    2.- Use of IF statements

@author: Alejandro Murrieta Mendoza
"""


class colors:
    cyan = "\033[96m"
    red = "\033[91m"
    yellow = "\033[93m"
    green = "\033[92m"
    end = "\033[0m"


morse = {
    "0": "-----",
    "1": "..---",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
}
if __name__ == "__main__":
    while True:
        user_input = input("Enter a number to translate, or type quit to exit the program: ")

        if user_input == "quit":
            exit()
        elif user_input not in morse.keys():
            print(f"{colors.red}ERROR:{colors.end} The input is not valid, please enter a valid character.")
            continue
        else:
            print(
                f"The number {colors.cyan}'{user_input}'{colors.end} in morse code is: {colors.cyan}'{morse[user_input]}'{colors.end}"
            )
