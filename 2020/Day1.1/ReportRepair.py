#!/usr/bin/python


expenses_list = []

expenses_file = open("PATH_TO_FILE", "r")

for line in expenses_file.readlines():
    line_int = int(line)
    expenses_list.append(line_int)

expenses_file.close()

add_to = 2020
hash_table = {}

for i in range(len(expenses_list)):
    complement = add_to - expenses_list[i]
    if complement in hash_table:
        print(expenses_list[i] * complement)
    hash_table[expenses_list[i]] = expenses_list[i]


