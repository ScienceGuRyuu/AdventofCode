from collections import Counter

custom_declorations_path = "/home/ryan/Documents/AdventOfCode/2020/Day6/custom_declorations.txt"
test_path = "/home/ryan/Documents/AdventOfCode/2020/Day6/test1.txt"

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def count_chars(text):
    counter = 0
    char_counter = Counter(text)
    for letter in letters:
        if letter in char_counter:
            counter += 1
    return counter

def get_group(file_path):
    group = ""
    sum_count = 0
    yes_count = 0
    people_in_group = 0
    with open(file_path) as decloration_form:
        for line in decloration_form:
            if line != '\n':
                group = group + line
                people_in_group += 1
            if line == '\n':
                sum_count += count_chars(group)
                yes_count += count_yes(group, people_in_group)
                #print("yes_count: ", yes_count)
                #input.txt()
                group = ""
                people_in_group = 0
    return sum_count, yes_count

def count_yes(text, people_in_group):
    yes_counts = 0
    chars_in_group = Counter(text)
    for key in list(chars_in_group): 
        if not key.isalpha():
            del chars_in_group[key]
    #print(chars_in_group)
    #print("people_in_group", people_in_group)
    for char_count in chars_in_group.values():
        if char_count == people_in_group:
            yes_counts += 1
    return yes_counts

                
print(get_group(custom_declorations_path))
print(get_group(test_path))
