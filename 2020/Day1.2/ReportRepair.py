#!/usr/bin/python


expenses_list = []

expenses_file = open("/home/ryan/Documents/AdventOfCode/2020/Day1.1/data.txt", "r")

for line in expenses_file.readlines():
    line_int = int(line)
    expenses_list.append(line_int)

expenses_file.close()

add_to = 2020
hash_table = {}

for i in range(len(expenses_list) - 1):
    complement = add_to - expenses_list[i]
    for j in range(i + 1, len(expenses_list)):
        if complement - expenses_list[j] in hash_table:
            print(expenses_list[j] * (complement - expenses_list[j]) * expenses_list[i])
        hash_table[expenses_list[i]] = expenses_list[i]



