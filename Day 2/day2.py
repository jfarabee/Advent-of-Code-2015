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
    smallest_measures=sorted([l, w, h])[:2]
    ribbon_length += (2*smallest_measures[0] + 2*smallest_measures[1])
    ribbon_length += l*w*h


print('Total surface area: ', surface_area, ' sqft.')
print('Total ribbon length: ', ribbon_length, ' ft.')
