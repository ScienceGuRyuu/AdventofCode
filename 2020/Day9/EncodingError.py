from itertools import combinations

preamble_list_path = "PATH_TO_FILE"
test_list_path = "PATH_TO_FILE"


class Encoder:
    def __init__(self, file_path, preamble_length, ignore_length):
        self.preamble_length = preamble_length
        self.ignore_length = ignore_length
        self.file_path = file_path
        self.xmas_list = []
        self.contiguous_list = []
        self.error_number = -1
        self.min_plus_max = 0
        self.get_list()

    def get_list(self):
        with open(self.file_path, "r") as f:
            for line in f:
                integer_input = int(line)
                self.xmas_list.append(integer_input)
        return self.xmas_list

    def find_first_error(self):
        for x in range(self.preamble_length, len(self.xmas_list)):
            integer_to_match = self.xmas_list[x]
            check_for_match_list = self.xmas_list[x - self.preamble_length: x]
            combos = [pair for pair in combinations(check_for_match_list, 2) if sum(pair) == integer_to_match]
            if len(combos) == 0:
                self.error_number = integer_to_match
                return False
        return True

    def find_contiguous_list_with_failed_number(self):
        starting_list_position = -1
        is_contiguous_list = False
        sum_of_list = 0
        contiguous_list = []
        while not is_contiguous_list:
            starting_list_position += 1
            if starting_list_position == len(self.xmas_list):
                break
            for x in range(starting_list_position, len(self.xmas_list)):
                if is_contiguous_list:
                    return True
                sum_of_list += self.xmas_list[x]
                contiguous_list.append(self.xmas_list[x])
                print(contiguous_list)
                if sum_of_list == self.error_number:
                    self.contiguous_list = contiguous_list
                    is_contiguous_list = True
                if sum_of_list > self.error_number:
                    contiguous_list = []
                    sum_of_list = 0
                    break
        return True

    def calculate_min_plus_max(self):
        self.find_contiguous_list_with_failed_number()
        self. min_plus_max = max(self.contiguous_list) + max(self.contiguous_list)
        print(min(self.contiguous_list) + max(self.contiguous_list))
        return True


def main():
    tester = Encoder(preamble_list_path, 25, 25)
    tester.find_first_error()
    print("Failure number:", tester.error_number)
    tester.calculate_min_plus_max()


if __name__ == "__main__":
    main()
