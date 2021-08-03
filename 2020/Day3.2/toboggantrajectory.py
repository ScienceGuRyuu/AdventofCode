#!/usr/bin/python
import math

base_map_path = "PATH_TO_FILE"



with open(base_map_path) as base_map:
    listed_map = [line.split() for line in base_map]

def TobogganChecker(right, down):
    checking_x_index = 0
    tree_counter = 0
    checking_y_index = 0
    for i in range((int((len(listed_map) - 1) / down))):
        checking_y_index += down
        print(checking_y_index)
        if (checking_x_index + right) <= 10:
            checking_x_index += right
            print(checking_x_index)
        else:
            checking_x_index = (right) - (len(listed_map[0][0]) - checking_x_index)
        if listed_map[checking_y_index][0][checking_x_index] == '#':
            tree_counter += 1
    return tree_counter

print(TobogganChecker(1,1)  * TobogganChecker(3,1) * TobogganChecker(5,1) * TobogganChecker(7,1) * TobogganChecker(1,2)) 




