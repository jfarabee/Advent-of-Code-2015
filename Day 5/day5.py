#Advent of Code 2015 Day 5
#written by Jacob Farabee

file=open("d5input.txt", "r")

input_strings = ""

if file.mode == "r":
    input_strings = file.readlines()

nice_strings = 0
vowels = ['a', 'e', 'i', 'o', 'u']
substrings = ["ab", "cd", "pq", "xy"]

for string in input_strings:
    double = False
    vowels_cnt = 0
    substring = False
    increment = 0
    for char in string:
        if increment > 1:
            prev = string[increment - 1]
            if char == prev:
                double = True
            if string[(increment - 1):increment] in substrings:
                substring = True
        if char in vowels:
            vowels_cnt += 1
        increment += 1
    if vowels_cnt >= 3 and double and not substring:
        nice_strings += 1

print("Nice strings: ", nice_strings)
