#AOC 2015 Day 1
#by Jacob Farabee

file=open("d1input.txt", "r")

if file.mode == "r":
    input_string=file.read()

floor=0
char_count=1
in_basement=False

for char in input_string:
    if char == "(":
        floor+=1
    if char == ")":
        floor-=1
    if floor == -1 and not in_basement:
        in_basement=True
        print('Santa enters the basement at character ', char_count)
    char_count+=1

print('Final floor: ', floor)
