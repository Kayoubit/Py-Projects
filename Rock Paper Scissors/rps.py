#Here is a game of rock, paper, scissors

import os
from random import randint
from random import seed
import time

hand = ["rock", "paper", "scissors"]

def prompt(display="Press enter to continue.", require=False):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s

def game():
    w = 0
    l = 0
    while True:
        #w = 0
        #l = 0
        num = randint(0, 2)
        print("~~~~~~~ Hello and Welcome to my game.~~~~~~~~\n\nLets start with the rules")
        print("It's very simple actually. Just choose rock, paper, or scissors.")
        print("Once you've made your choice, press enter. I promise I won't cheat!")
        print("-------------------------------------------")
        print("| Your current score is " + str(w) + " wins and " + str(l) + " losses.|")
        print("-------------------------------------------")
        a = input("Choose a hand or type 'quit' to exit. ")
        print("Ready?!")
        time.sleep(2)
        print("rock")
        time.sleep(1)
        print("paper")
        time.sleep(1)
        print("scissors")
        time.sleep(1)
        print("shoot")
        b = hand[num]
        if a == str(b):
            print("Looks like we chose the same hand! Let's play again\n")
            prompt()
            os.system('cls')
        elif a == "rock" and str(b) == "paper":
            print("You lose! Paper covers rock.\n")
            l += 1
            prompt()
            os.system('cls')
        elif a == "rock" and str(b) == "scissors":
            print("You win! Rock crushes scissors.\n")
            w += 1
            prompt()
            os.system('cls')
        elif a == "paper" and str(b) == "rock":
            print("You win! Paper covers rock.\n")
            w += 1
            prompt()
            os.system('cls')
        elif a == "paper" and str(b) == "scissors":
            print("You lose! Scissors cut paper.\n")
            l += 1
            prompt()
            os.system('cls')
        elif a == "scissors" and str(b) == "rock":
            print("You lose! Rock crushes scissors.\n")
            l += 1
            prompt()
            os.system('cls')
        elif a == "scissors" and str(b) == "paper":
            print("You win! Scissors cut paper.\n")
            w += 1
            prompt()
            os.system('cls')
        else:
            break

game()
        
