#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:59:33 2022

challenge 1
Problem:
This is the typical paper/rock/scissors game. The user want to play n times 
this game against the computer. Every time the user has to introduce his/her and
and his/her hand is compared against the computer's hand. The input by the 
user should be verified to be valid. The result should be saved. When the 
n number of games are over, for every played game, the winner  and the compared 
hands should be displayed. Also the user's winning rate should be displayed.

Basic paper/rock/scissors rules apply:
Paper wins over rock
Rock wins over scissors.
Scissors win over paper.
Paper wins over rock. 

There are some proposed steps to follow to guide you. However, feel free to 
do it as you see fit. 

Objectives:
    - Pick a random value from a list
    - Use IF statements to determine the winner. 
    - Use a For Loop
    - Save Data in a List
    - Print the winner
@author: Alejandro Murrieta-Mendoza
"""

import random
from enum import Enum


class Choices(Enum):
    rock = 1
    paper = 2
    scissors = 3


class colors:
    cyan = "\033[96m"
    red = "\033[91m"
    yellow = "\033[93m"
    green = "\033[92m"
    end = "\033[0m"


def plays_prompt():
    try:
        plays = int(input("How many times do you want to play rock/paper/scissors?: "))
        return plays
    except ValueError:
        print(f"{colors.red}ERROR:{colors.end} The input is not a valid number, please try again.")
        return plays_prompt()


def player_prompt():
    try:
        print("Please select and option:")
        print("1: rock")
        print("2: paper")
        print("3: scissors")
        player_input = int(input("Please enter the number of your choice: "))

        if 0 < player_input < 4:
            return Choices(player_input)
        else:
            print(
                f"{colors.red}ERROR:{colors.end} The input is not a number between 1 and 3, please input a valid number."
            )
            return player_prompt()
    except ValueError:
        print(f"{colors.red}ERROR:{colors.end} The input is not a number between 1 and 3, please input a valid number.")
        return player_prompt()


def determine_winner(player_hand, bot_hand):
    if (
        (player_hand == Choices.rock and bot_hand == Choices.scissors)
        or (player_hand == Choices.paper and bot_hand == Choices.rock)
        or (player_hand == Choices.scissors and bot_hand == Choices.paper)
    ):
        return "win"
    elif player_hand == bot_hand:
        return "tie"
    else:
        return "loss"


if __name__ == "__main__":
    game_status = {"win": 0, "tie": 0, "loss": 0}

    plays = plays_prompt()

    for i in range(plays):
        player_hand = player_prompt()
        bot_hand = Choices(random.randint(1, 3))

        round_result = determine_winner(player_hand, bot_hand)
        game_status[round_result] += 1

        print(
            f"You chose {colors.cyan}{player_hand.name}{colors.cyan}{colors.end}, the bot chose {colors.cyan}{bot_hand.name}{colors.end}"
        )
        print(
            f"This round resulted in a {colors.green if round_result == 'win' else colors.yellow if round_result == 'tie' else colors.red  }{round_result}{colors.end} \n"
        )

    print(f"{colors.cyan}*GAME ENDED*{colors.end}")
    print("Results of this game:")
    print(f"Nr. of wins: {colors.green}{game_status['win']}{colors.end}, ratio: {game_status['win'] / plays * 100}%")
    print(f"Nr. of ties: {colors.yellow}{game_status['tie']}{colors.end}, ratio: {game_status['tie'] / plays * 100}%")
    print(f"Nr. of losses: {colors.red}{game_status['loss']}{colors.end}, ratio: {game_status['loss'] / plays * 100}%")

    if game_status["win"] > game_status["loss"]:
        print(f"You won this game, {colors.green}CONGRATULATIONS!{colors.end}")
    elif game_status["win"] == game_status["loss"]:
        print(f"The game ended in a tie, {colors.yellow}no winners or losers here.{colors.end}")
    else:
        print(f"You lost this game, {colors.red}better luck next time!{colors.end}")
