#Advent of Code 2015 Day 2
#written by Jacob Farabee

file=open("d2input.txt", "r")

input_strings=file.readlines()

surface_area=0
ribbon_length=0

for input in input_strings:
    nums=input.split('x')
    l, w, h = int(nums[0]), int(nums[1]), int(nums[2])
    surface_area += (2*l*w + 2*w*h + 2*h*l) + min((l*w), (w*h), (h*l))

print('Total surface area: ', surface_area, ' sqft.')
