from collections import defaultdict

short_test_path = "PATH_TO_FILE"
long_test_path = "PATH_TO_FILE"
input_path = "PATH_TO_FILE"


class ShockMaster:
    def __init__(self, file_path):
        self.file_path = file_path
        self.adaptors_list = []
        self.count_of_differences_dict = defaultdict(int)
        self.organize_data()

    def organize_data(self):
        with open(self.file_path) as file:
            for line in file:
                data_line = int(line)
                self.adaptors_list.append(data_line)
        self.adaptors_list.append(0)
        self.adaptors_list.sort()
        internal_adapter = self.adaptors_list[-1] + 3
        self.adaptors_list.append(internal_adapter)

    def count_differences(self):
        for i in range(len(self.adaptors_list)):
            if i == 0:
                difference_in_joltage = self.adaptors_list[i]
            else:
                difference_in_joltage = self.adaptors_list[i] - self.adaptors_list[i - 1]
            self.count_of_differences_dict[difference_in_joltage] += 1
        return self.count_of_differences_dict

    def multiply_differences_in_one_and_three(self):
        product_of_counts_of_1_and_3 = self.count_of_differences_dict[1] * self.count_of_differences_dict[3]
        return product_of_counts_of_1_and_3

    def dynamic_search(self):
        ways = defaultdict(lambda: 0)
        goal = max(self.adaptors_list)
        ways[goal] = 1
        joltages = list(map(int, self.adaptors_list))
        for n in sorted(joltages, reverse=True)[1:]:
            ways[n] = ways[n + 1] + ways[n + 2] + ways[n + 3]
        return ways[0]


def main():
    shocker = ShockMaster(input_path)
    shocker.count_differences()
    answer_part_1 = shocker.multiply_differences_in_one_and_three()
    print(answer_part_1)
    part_2 = shocker.dynamic_search()
    print(part_2)


if __name__ == "__main__":
    main()
