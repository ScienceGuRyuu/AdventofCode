batch_file_path = "/home/ryan/Documents/AdventOfCode/2020/Day4.1/batch_file.txt"

def clean_file(passport_file):
    pass_list = make_into_list(passport_file)
    pass_dict = [make_into_dict(item) for item in pass_list]
    #print(pass_dict)
    return pass_dict

def make_into_list(passport_file):
    list_of_passports = []
    with open(batch_file_path) as passport_file:
        for line in passport_file:
            list_of_passports.append(line) 
    string_of_passports = "".join(list_of_passports)
    split_passports = string_of_passports.split("\n\n")
    #print(split_passports)
    split2_passports = [split_passports[0].replace("\n", " ") for string in split_passports]
    #print(split2_passports)
    split3_passports = [string.split() for string in split2_passports]
    #print(split3_passports)
    return split3_passports

def make_into_dict(list_of_passports):
    passport_dict = {}
    for item in list_of_passports:
        item_parts = item.split(":")
        key = item_parts[0]
        value = item_parts[1]
        passport_dict[key] = value
    return passport_dict

def is_valid_passport(passport):
    has_birth_year = "byr" in passport
    has_issue_year = "iyr" in passport
    has_expiration_year = "eyr" in passport
    has_height = "hgt" in passport
    has_hair_color = "hcl" in passport
    has_eye_color = "ecl" in passport
    has_passport_id = "pid" in passport
    has_country_id = "cid" in passport
    return (has_birth_year and has_issue_year and has_expiration_year and has_height and has_hair_color and has_eye_color and has_passport_id)

def has_valid_values(passport):
    has_valid_birth_year = 1920 <= int(passport["byr"]) <= 2002
    has_valid_issue_year = 2010 <= int(passport["iyr"]) <= 2020
    has_valid_expiration_year = 2020 <= int(passport["eyr"]) <= 2030
    
    has_valid_height = False
    height_units = passport["hgt"][-2:]
    if height_units == "cm":
        height = int(passport["hgt"][:-2])
        has_valid_height = 150 <= height <= 193
    elif height_units == "in":
        height = int(passport["hgt"][:-2])
        has_valid_height = 59 <= height <= 76
        
    def is_valid_hex_string(string):
        test_value = string.lower()
        is_valid = True
 
        for character in string:
            if character not in "0123456789abcdef":
                is_valid = False
                break
 
        return is_valid
        
    has_valid_hair_color = False
    if len(passport["hcl"]) == 7:
        digits = passport["hcl"][1:]
        has_valid_hair_color = is_valid_hex_string(digits)
            
    has_valid_eye_color = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    def is_valid_passport_id(value):
        is_valid = False
        
        if len(value) == 9:
            is_valid = True
 
            for character in value:
                if character not in "0123456789":
                    is_valid = False
                    break
        
        return is_valid
    
    has_valid_passport_id = is_valid_passport_id(passport["pid"])
                
        
    return (
        has_valid_birth_year and
        has_valid_issue_year and
        has_valid_expiration_year and
        has_valid_height and
        has_valid_hair_color and
        has_valid_eye_color and
        has_valid_passport_id
    )

