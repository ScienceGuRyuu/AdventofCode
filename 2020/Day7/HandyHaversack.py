import input as ip
import re

def bag_data_structure(initial_data):
    result = {}
    
    for item in initial_data:
        bag_and_contents_regex = r"^(\w+ \w+) bags contain (.*)"
        bag_and_contents = re.search(bag_and_contents_regex, item)
        bag_type = bag_and_contents[1]
        
        contents_string = bag_and_contents[2][:-1] # [:-1] removes trailing period
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

bag_data_structure(ip.main_raw_input)
