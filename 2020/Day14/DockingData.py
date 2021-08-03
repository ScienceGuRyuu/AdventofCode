import re
import itertools

instruction_file_path = "PATH_TO_FILE"


class Machine:
    def __init__(self, file_path):
        self.file_path = instruction_file_path
        self.list_of_instructions = []
        self.make_instructions()

    def make_instructions(self):
        for line in open(self.file_path):
            line = line.strip('\n')
            self.list_of_instructions.append(line)

    def execute_instructions(self, list_of_instructions):
        mask = re.sub("mask = ", "", list_of_instructions[0])
        instructions = list_of_instructions[1:]
        for i in range(len(instructions)):
            address_and_value = re.findall("\d+", instructions[i])
            instructions[i] = address_and_value
        for value in instructions:
            int_value = int(value[1])
            binary_value_string = '{0:036b}'.format(int_value)
            value_to_use = binary_value_string
            for i in range(len(binary_value_string)):
                if mask[i] != "X":
                    value_to_use = value_to_use[:i] + mask[i] + value_to_use[i+1:]
                    print(value_to_use)
                elif mask[i] == 'X':
                    value_to_use = value_to_use[:i] + binary_value_string[i] + value_to_use[i+1:]
                    print(value_to_use)







def main():
    finder = Machine(instruction_file_path)
    finder.execute_instructions(finder.list_of_instructions)


if __name__ == "__main__":
    main()
