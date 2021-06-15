#!/usr/bin/python

base_map_path = '/home/ryan/Documents/AdventOfCode/2020/Day3.1/base_map.txt'

tree_counter = 0
previous_y_index = 0


with open(base_map_path) as base_map:
    listed_map = [line.split() for line in base_map]

for i in range(len(listed_map)-1):
    print(i)
    print(previous_y_index)
    input()
    if previous_y_index == 28:
        if listed_map[i+1][0][0] == '#':
            tree_counter += 1    
            previous_y_index = 0  
        else:
            previous_y_index = 0
    elif previous_y_index == 29:
        if listed_map[i+1][0][1] == '#':
            tree_counter += 1
            previous_y_index = 1
        else:
            previous_y_index = 1
    elif previous_y_index == 30:  
        if listed_map[i+1][0][2] == '#':
            tree_counter += 1
            previous_y_index = 2
        else:
            previous_y_index = 2
    else:
        if listed_map[i+1][0][previous_y_index+3] == '#':
            tree_counter += 1
            previous_y_index += 3
        else:
            previous_y_index += 3

print(tree_counter)

