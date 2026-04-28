#This is a test game file. Not sure what I'm gonna do here but trying to implement some different elements.

import os
from random import randint
from random import seed

def prompt(display="Press enter to continue.", require=False):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s

def game():
    while True:
        num = randint(1, 10)
        print("Hello and welcome to my game.\nLets start by you trying to guess what number I'm thinking of.")
        a = input("Go ahead, between 1 - 10 what number am I thinking of? ")
        if a == str(num):
            print("That is correct!")
            prompt()
        else:
            print("That is not correct!")
            print("The correct number was " + str(num) + "!")
            b = input("Would you like to play again? ")
            if b == "yes":
                prompt()
            else:
                break

game()