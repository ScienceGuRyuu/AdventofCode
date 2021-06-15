import re

batch_file_path = "/home/ryan/Documents/AdventOfCode/2020/Day4.1/batch_file.txt"

class Validation:
    def __init__(self, passport_file):
        with open(passport_file):
            self.passport_library = self.striper(passport_file)
        print(self.passport_library)
        input()
    def check_feild_count(self):
        is_proper_length = len(self.passport) == 8 or (len(self.passport) == 7 and 'cid' not in self.passport)
        print ("len: ", len(self.passport), is_proper_length)
        print(self.passport)
        return is_proper_length
    
    def check_year_range(self, key, first, last):
        is_within_range = len(self.passport) == 4 and int(self.passport[key]) >=first and int(self.passport[key]) <= last
        print ("range: ", is_within_range)
        return is_within_range

    def check_byr(self):
        is_valid_byr = self.check_year_range('byr', 1920, 2002)
        print ("byr:", is_valid_byr)
        return is_valid_byr

    def check_iyr(self):
        is_valid_iyr = self.check_year_range('iyr', 2010, 2020)
        print ("iyr: ", is_valid_iyr)
        return is_valid_iyr

    def check_eyr(self):
        is_valid_eyr = self.check_year_range('eyr', 2020, 2030)
        print("eyr:", is_valid_eyr)
        return is_valid_eyr

    def check_hgt(self):
        is_valid_hgt = False
        if self.passport['hgt'][-2:] == 'cm':
            if int(self.passport['hgt'][:-2]) >= 150 and int(self.passport['hgt'][:-2]) <= 190:
                is_valid_hgt = True
        elif self.passport['hgt'][-2:] == 'in':
            if int(self.passport['hgt'][:-2]) >= 59 and int(self.passport['hgt'][:-2]) <= 76:
                is_valid_hgt = True
        print("hgt: ", is_valid_hgt)
        return is_valid_hgt

    def check_hcl(self):
        is_valid_hcl = False
        if self.passport['hcl'][0] == '#' and len(self.passport['hcl'][:1] == 6):
            is_valid_hcl = re.search("[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]", self.passport['hcl'][1:])
        print("hcl: ", is_valid_hcl)
        return is_valid_hcl

    def check_ecl(self):
        is_valid_ecl = self.passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        print("ecl: ", is_valid_ecl)
        return is_valid_ecl

    def check_pid(self):
        is_valid_pid = False
        if len(self.passport['pid'][0:]) == 9:
            is_valid_pid = True
        print("pid: ", is_valid_pid)
        return is_valid_pid

    def check_passport_validity(self):
        result = self.check_feild_count() and self.check_pid() and self.check_ecl() and self.check_hcl() and self.check_hcl() and self.check_hgt() and self.check_eyr() and self.check_iyr() and self.check_byr()
        print("result", result)
        input()
        return result

    def striper(self, input_file):
        passport_list = []
        passport_library = {}
        for line in input_file:
            if line != "\n":
                line = line.rstrip().split(" ")
                line = [field.split(":") for field in line]
                for field in line:
                    passport[field[0]] = field[1]
            else:
                passports.append(passport)
                passport = {}
        passports.append(passport)
        return passports

test = Validation(batch_file_path) 

