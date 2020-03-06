#Advent of Code 2015 Day 6
#written by Jacob Farabee

import numpy as np

def turn_on(coord_a, coord_b):
    

file = open("d6input.txt", "r")

input_strings = ""

if file.mode == "r":
    input_strings = file.readlines()

for string in input_strings:
    action = string[0:9]
    coord_a = string[10:16]
    coord_b = string[25:32]
    if action == "turn on  ":

    elif action == "turn off ":

    elif action == "toggle   ":
