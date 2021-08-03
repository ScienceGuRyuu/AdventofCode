import re

data_path = "PATH_TO_FILE"


def bag_data_structure(file_path):
    result = {}
    with open(file_path) as initial_data:
        for item in initial_data:
            bag_and_contents = re.search(r"^(\w+ \w+) bags contain (.*)", item)
            bag_type = bag_and_contents[1]
            contents_string = bag_and_contents[2][:-1] 
            contents_regex = r"([0-9] )*(\w+ \w+) bag"
            contents_tuples = re.findall(contents_regex, contents_string)
        
            bag_contents = []
            for contents_tuple in contents_tuples:
                if contents_tuple[1] != "no other":
                    bag_contents.append({
                        "count": int(contents_tuple[0]),
                        "type": contents_tuple[1]
                 })   
            result[bag_type] = bag_contents
    return result

def count_shiny_gold(bag_data_structure, bag_name):
    shiny_gold_count = 0
    bag = bag_data_structure[bag_name]
    if len(bag) == 0:
        return shiny_gold_count
    else:
        for inner_bag in bag:
            if inner_bag["type"] == "shiny gold":
                shiny_gold_count += 1
            shiny_gold_count += count_shiny_gold(bag_data_structure, inner_bag["type"])
    return shiny_gold_count

def count_bags_with_one_plus_shiny_gold_bags(bag_data_structure):
    count = 0
    for bag_name in bag_data_structure.keys():
        if count_shiny_gold(bag_data_structure, bag_name) > 0:
            count += 1
    return count

def bag_count(bag_data_structure, bag_name):
    count = 0
    top_level_name = bag_data_structure[bag_name]
    if len(top_level_name) == 0:
        return count
    else:
        for current_bag in top_level_name:
            current_bag_count = current_bag["count"]
            count += current_bag_count
            nested_bags_count = bag_count(bag_data_structure, current_bag["type"]) 
            count += nested_bags_count * current_bag_count
    return count

bags = bag_data_structure(data_path)
number_bags_with_shiny_gold = count_bags_with_one_plus_shiny_gold_bags(bags)
print(number_bags_with_shiny_gold)
print(bag_count(bags, "shiny gold"))
