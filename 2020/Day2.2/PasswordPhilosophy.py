#!/usr/bin/python

import re

expenses_file = open("/home/ryan/Documents/AdventOfCode/2020/Day2.1/passwords.txt", "r")

number_of_valid_passwords = 0

for line in expenses_file.readlines():
    range_list = re.findall("\d+", line)
    char_of_interest = re.findall("[a-z]:", line)
    target_char = char_of_interest[0][0]
    position1 = int(range_list[0]) + 1
    position2 = int(range_list[1]) + 1
    password = re.findall(":\s[a-z]+", line)[0]
    number_of_matches = 0
    if (password[position1] == char_of_interest and password[position2] != char_of_interest): #or (password[position1] != char_of_interest and password[position2] == char_of_interest):
        number_of_matches +=1
    break
expenses_file.close()

print (number_of_matches)




