#Advent of Code 2015 Day 3
#written by Jacob Farabee

file=open("d3input.txt", "r")

input_string = ""

if file.mode == "r":
    input_string = file.read()

santa_x, santa_y = 0, 0

    #initialize dictionary w/ first house (0,0), which gets one present
houses = {
    str(santa_x)+','+str(santa_y) : 1
}

for char in input_string:
    if char == '^':
        santa_y += 1
        if str(santa_x)+','+str(santa_y) in houses:
            houses[str(santa_x)+','+str(santa_y)] += 1
        else:
            houses[str(santa_x)+','+str(santa_y)] = 1
    if char == 'v':
        santa_y -= 1
        if str(santa_x)+','+str(santa_y) in houses:
            houses[str(santa_x)+','+str(santa_y)] += 1
        else:
            houses[str(santa_x)+','+str(santa_y)] = 1
    if char == '>':
        santa_x += 1
        if str(santa_x)+','+str(santa_y) in houses:
            houses[str(santa_x)+','+str(santa_y)] += 1
        else:
            houses[str(santa_x)+','+str(santa_y)] = 1
    if char == '<':
        santa_x -= 1
        if str(santa_x)+','+str(santa_y) in houses:
            houses[str(santa_x)+','+str(santa_y)] += 1
        else:
            houses[str(santa_x)+','+str(santa_y)] = 1

lucky_houses=0

for coord, presents in houses.items():
    if presents > 1:
        lucky_houses += 1

print("Number of lucky houses: ", lucky_houses)
