#!/usr/bin/python

import re

expenses_file = open("PATH_TO_FILE", "r")

number_of_valid_passwords = 0

for line in expenses_file.readlines():
    range_list = re.findall("\d+", line)
    char_of_interest = re.findall("[a-z]:", line)
    target_char = char_of_interest[0][0]
    min_allowed = int(range_list[0])
    max_allowed = int(range_list[1])
    password = re.findall(":\s[a-z]+", line)[0]
    number_of_matches = 0
    i = 0
    for char in password:
        if password[i] == target_char:
            number_of_matches += 1
        i += 1
    if number_of_matches in range(min_allowed, max_allowed + 1):
        number_of_valid_passwords += 1
expenses_file.close()

print (number_of_valid_passwords)

