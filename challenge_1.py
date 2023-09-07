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

import os
import random
from enum import Enum


class Choices(Enum):
    rock = 1
    paper = 2
    scissors = 3


class colors:
    cyan_char = "\033[96m"
    red_char = "\033[91m"
    yellow_char = "\033[93m"
    green_char = "\033[92m"
    end_char = "\033[0m"

    def green(string):
        return f"{colors.green_char}{string}{colors.end_char}"

    def red(string):
        return f"{colors.red_char}{string}{colors.end_char}"

    def yellow(string):
        return f"{colors.yellow_char}{string}{colors.end_char}"

    def cyan(string):
        return f"{colors.cyan_char}{string}{colors.end_char}"


ascii_text = """
  ____   ___   ____ _  __  ____   _    ____  _____ ____    ____   ____ ___ ____ ____   ___  ____  ____  
 |  _ \ / _ \ / ___| |/ / |  _ \ / \  |  _ \| ____|  _ \  / ___| / ___|_ _/ ___/ ___| / _ \|  _ \/ ___| 
 | |_) | | | | |   | ' /  | |_) / _ \ | |_) |  _| | |_) | \___ \| |    | |\___ \___ \| | | | |_) \___ \ 
 |  _ <| |_| | |___| . \  |  __/ ___ \|  __/| |___|  _ <   ___) | |___ | | ___) |__) | |_| |  _ < ___) |
 |_| \_\\\___/ \____|_|\_\ |_| /_/   \_\_|   |_____|_| \_\ |____/ \____|___|____/____/ \___/|_| \_\____/                                                                                                         
"""

ascii_art = """
            _______                   _______                               _______
        ---'   ____)              ---'   ____)____                      ---'   ____)____  
              (_____)                       ______)                               ______)  
              (_____)                       _______)                           __________)  
              (____)                       _______)                           (____)
        ---.__(___)               ---.__________)                       ---.__(___)  

"""


def plays_prompt():
    try:
        plays = int(input("How many times do you want to play rock/paper/scissors?: "))
        return plays
    except ValueError:
        print(f"{colors.red('ERROR:')} The input is not a valid number, please try again.")
        return plays_prompt()


def player_prompt(round_nr):
    try:
        print(f"{colors.cyan(f'[ROUND {round_nr}] ')}Please select and option:")
        print(f"{Choices(1).value}: {Choices(1).name}")
        print(f"{Choices(2).value}: {Choices(2).name}")
        print(f"{Choices(3).value}: {Choices(3).name}")
        player_input = int(input("Please enter the number of your choice: "))

        if 0 < player_input < 4:
            return Choices(player_input)
        else:
            print(f"{colors.red('ERROR:')} The input is not a number between 1 and 3, please input a valid number.")
            return player_prompt(round_nr)
    except ValueError:
        print(f"{colors.red('ERROR:')} The input is not a number between 1 and 3, please input a valid number.")
        return player_prompt(round_nr)


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

    os.system("cls" if os.name == "nt" else "clear")
    print(colors.red("=" * 105), end="")
    print(colors.cyan(ascii_text), end="")
    print(colors.cyan(ascii_art), end="")
    print(colors.red("=" * 105))

    plays = plays_prompt()

    for i in range(plays):
        player_hand = player_prompt(i + 1)
        bot_hand = Choices(random.randint(1, 3))

        round_result = determine_winner(player_hand, bot_hand)
        game_status[round_result] += 1

        print(f"You chose {colors.cyan(player_hand.name)}, the bot chose {colors.cyan(bot_hand.name)}")
        print(
            f"This round resulted in a {colors.green(round_result) if round_result == 'win' else colors.yellow(round_result) if round_result == 'tie' else colors.red(round_result)}\n"
        )

    print(colors.cyan("!GAME ENDED!"))
    print("Results of this game:")
    print(f"Nr. of wins: {colors.green(game_status['win'])}, ratio: {round(game_status['win'] / plays * 100, 2)}%")
    print(f"Nr. of ties: {colors.yellow(game_status['tie'])}, ratio: {round(game_status['tie'] / plays * 100, 2)}%")
    print(f"Nr. of losses: {colors.red(game_status['loss'])}, ratio: {round(game_status['loss'] / plays * 100, 2)}%")

    if game_status["win"] > game_status["loss"]:
        print(f"You won this game, {colors.green('CONGRATULATIONS!')}")
    elif game_status["win"] == game_status["loss"]:
        print(f"The game ended in a tie, {colors.yellow('no winners or losers here.')}")
    else:
        print(f"You lost this game, {colors.red('better luck next time!')}")
