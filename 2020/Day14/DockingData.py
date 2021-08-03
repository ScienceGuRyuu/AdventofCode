import re

instruction_file_path = '/home/ryan/Documents/AdventOfCode/2020/Day14/program.txt'
instruction_file_path = '/home/ryan/Documents/AdventOfCode/2020/Day14/test.txt'

class Machine:
    def __init__(self, file_path):
        self.file_path = instruction_file_path
        self.list_of_instructions = []
        self.make_instructions()

    def make_instructions(self):
        with open(self.file_path) as f:
            lines = f.readlines()
            last_line = lines[-1]
            first_line = lines[0]
            mask = ''
            list_of_instructions = []
            for line in f:
                if line == last_line:
                    self.list_of_instructions.append([mask, list_of_instructions])
                elif re.match("mask", line):
                    if line != first_line:
                        self.list_of_instructions.append([mask, list_of_instructions])
                        list_of_instructions = []
                    mask = re.sub("mask = ", "", line)
                elif re.match("mem", line):
                    list_of_instructions.append(re.findall('\d+', line))


def main():
    finder = Machine(instruction_file_path)
    print(finder.list_of_instructions)


if __name__ == "__main__":
    main()
