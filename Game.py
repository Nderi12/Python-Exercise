#!/usr/bin/env python3

import random

number = random.randint(1, 10) #return random integers from low to high
tries = 1

u_name = input("Hello, what is your username?")
print("Hello", u_name+ ",", )

question = input("Would you like to play a game?[Y/N]")
if question == "N":
    print("oh..okay")

if question == "Y":
    print("I'm thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))
    if guess < number:
        print("Guess lower...")
if guess < number:
    print("Guess higher...")
    while guess != number:
        tries += 1
        guess = int(input("Try again: "))
        if guess < number:
            print("Guess Higher")
    if guess == number:
        print("You're right! You win! The number was {}  and its only {} tries".format(number, tries))