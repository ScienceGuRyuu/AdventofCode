instruction_file_path = "PATH_TO_FILE"


class AutoPilot:
    def __init__(self, instructions):
        self.facing_direction = 90
        self.file_path = instructions
        self.instructions = self.make_instructions()
        self.plane_location = [0, 0]
        self.waypoint_location = [10, 1]
        self.plane_location_history = [[0, 0]]
        self.waypoint_location_history = [[10, 1]]

    def make_instructions(self):
        instructions = []
        with open(self.file_path) as directions:
            for command in directions:
                directional = command[0]
                magnitude = int(command[1:].strip())
                split_command = [directional, magnitude]
                instructions.append(split_command)
        return instructions

    def execute_instructions_part_1(self):
        for instruction in self.instructions:
            directional, magnitude = instruction[0], instruction[1]
            if directional == 'N':
                self.plane_location[1] += magnitude
            if directional == 'E':
                self.plane_location[0] += magnitude
            if directional == 'S':
                self.plane_location[1] += -magnitude
            if directional == 'W':
                self.plane_location[0] += -magnitude
            if directional == 'L':
                self.facing_direction += -magnitude
            if directional == 'R':
                self.facing_direction += magnitude
            if directional == 'F':
                self.calculate_forward_1(magnitude)
            self.plane_location_history.append(self.plane_location)
            self.waypoint_location_history.append(self.waypoint_location)
        return self.plane_location_history, self.waypoint_location_history

    def calculate_forward_1(self, magnitude):
        if self.facing_direction % 360 == 0:
            self.plane_location[1] += magnitude
        if self.facing_direction % 360 == 90:
            self.plane_location[0] += magnitude
        if self.facing_direction % 360 == 180:
            self.plane_location[1] += -magnitude
        if self.facing_direction % 360 == 270:
            self.plane_location[0] += -magnitude

    def calculate_manhattan_distance(self):
        e_w = self.plane_location[0]
        n_s = self.plane_location[1]
        return abs(n_s) + abs(e_w)

    def execute_instructions_part_2(self):
        for instruction in self.instructions:
            directional, magnitude = instruction[0], instruction[1]
            if directional == 'N':
                self.waypoint_location[1] += magnitude
            if directional == 'E':
                self.waypoint_location[0] += magnitude
            if directional == 'S':
                self.waypoint_location[1] += -magnitude
            if directional == 'W':
                self.waypoint_location[0] += -magnitude
            if directional == 'L':
                self.do_turn(magnitude, directional)
            if directional == 'R':
                self.do_turn(magnitude, directional)
            if directional == 'F':
                self.calculate_forward_2(magnitude)
            self.plane_location_history.append(self.plane_location)
            self.waypoint_location_history.append(self.waypoint_location)
        return self.plane_location_history, self.waypoint_location_history

    def do_turn(self, magnitude, direction):
        if (direction == "L" and magnitude == 90) or (direction == "R" and magnitude == 270):
            self.waypoint_location = [-self.waypoint_location[1], self.waypoint_location[0]]
        if magnitude == 180:
            self.waypoint_location = [-self.waypoint_location[0], -self.waypoint_location[1]]
        if (direction == "L" and magnitude == 270) or (direction == "R" and magnitude == 90):
            self.waypoint_location = [self.waypoint_location[1], -self.waypoint_location[0]]

    def calculate_forward_2(self, magnitude):
        move_list = [x * magnitude for x in self.waypoint_location]
        self.plane_location = [a + b for a, b in zip(move_list, self.plane_location)]


def main():
    # captain = AutoPilot(instruction_file_path)
    # captain.execute_instructions_part_1()
    # manhattan_distance = captain.calculate_manhattan_distance()
    # print("manhattan_distance:", manhattan_distance)
    captain2 = AutoPilot(instruction_file_path)
    captain2.execute_instructions_part_2()
    manhattan_distance2 = captain2.calculate_manhattan_distance()
    print("manhattan_distance:", manhattan_distance2)


if __name__ == "__main__":
    main()
