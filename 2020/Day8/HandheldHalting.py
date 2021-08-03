instruction_path = '/home/ryan/Documents/AdventOfCode/2020/Day8/instruction.txt'


# instruction_path = '/home/ryan/Documents/AdventOfCode/2020/Day8/test_seats.txt'

def make_action_data_structure(instruction_path):
    instructions = []
    with open(instruction_path) as instruction_file:
        for line in instruction_file:
            instruction = {}
            opcode_operand = line.split()
            instruction["opcode"] = opcode_operand[0]
            instruction["operand"] = int(opcode_operand[1])
            instructions.append(instruction)
    return instructions


def run_through_boot(instruction_data_structure):
    program_length = len(instruction_data_structure)
    line_counter = 0
    accumulator = 0
    read_lines = []
    repeated_lines = False
    while 0 <= line_counter <= program_length:
        current_instruction = instruction_data_structure[line_counter]
        if line_counter in read_lines:
            repeated_lines = True
            break
        else:
            read_lines.append(line_counter)
        if current_instruction["opcode"] == "jmp":
            line_counter += current_instruction["operand"]
            continue
        elif current_instruction["opcode"] == "acc":
            accumulator += current_instruction["operand"]
        elif current_instruction["opcode"] == "nop":
            pass
        line_counter += 1
    return accumulator, repeated_lines


def change_boot_opcodes(instruction_data_structure):
    INITIAL_DATA_STRUCTURE = instruction_data_structure
    test_data_structure = instruction_data_structure
    last_line_changed = 0
    test_line = 0
    accumulator, repeating_lines = run_through_boot(test_data_structure)
    print(accumulator, repeating_lines)
    input()
    while repeating_lines:
        for item in test_data_structure:
            test_line += 1
            test_data_structure = INITIAL_DATA_STRUCTURE
            if item["opcode"] == "jmp" and test_line > last_line_changed:
                item["opcode"] = "nop"
                print(item["opcode"])
                print("Changed jmp to nop on line ", test_line)
                accumulator, repeating_lines = run_through_boot(test_data_structure)
                print(accumulator, repeating_lines)
                input()
            elif item["opcode"] == "nop" and test_line > last_line_changed:
                item["opcode"] = "jmp"
                print(item["opcode"])
                print("Changed nop to jmp on line ", test_line)
                accumulator, repeating_lines = run_through_boot(test_data_structure)
                print(accumulator, repeating_lines)
                input()


def accumulator_value_and_halt_at_first_repeat(instructions, switch_opcode_address=-1):
    program_length = len(instructions)
    program_counter = 0
    accumulator = 0
    executed_instructions = set()

    while 0 <= program_counter < program_length:
        current_instruction = instructions[program_counter]

        if program_counter in executed_instructions:
            return {
                "halted": False,
                "program_counter": program_counter,
                "accumulator": accumulator
            }
        else:
            executed_instructions.add(program_counter)

        opcode = current_instruction["opcode"]
        operand = current_instruction["operand"]

        if program_counter == switch_opcode_address:
            print(f"Changing opcode at address {program_counter}")
            if opcode == "jmp":
                print("- Changing jmp to nop")
                opcode = "nop"
            elif opcode == "nop":
                print("- Changing nop to jmp")
                opcode = "jmp"

        if opcode == "jmp":
            program_counter += operand
            continue
        elif opcode == "acc":
            accumulator += operand
        elif opcode == "nop":
            pass
        else:
            print("Something went wrong in accumulator_value_at_first_repeated_instruction().")
            print(f"pc = {program_counter} acc = {accumulator}")

        program_counter += 1

    return {
        "halted": True,
        "program_counter": program_counter,
        "accumulator": accumulator
    }


def run_instructions_with_mods(program):
    for index in range(len(program)):
        instruction = program[index]
        if instruction["opcode"] != "acc":
            print(f"Found jmp or nop at address: {index}")
            result = accumulator_value_and_halt_at_first_repeat(program, index)
            if result["halted"]:
                print(f"Found it! {result}")
                break
            else:
                print(f"Not the correct instruction.")


boot_data = make_action_data_structure(instruction_path)
print(run_through_boot(boot_data))
run_instructions_with_mods(boot_data)



