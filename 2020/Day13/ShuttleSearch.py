import re
from math import ceil, prod

instruction_file_path = "PATH_TO_FILE"


class Scheduler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.target_time = 0
        self.bus_ids = []
        self.bus_id_info_dict = {}
        self.make_schedule()

    def make_schedule(self):
        with open(self.file_path) as file:
            self.target_time = int(file.readline())
            busses = file.readline()
        busses = re.split(",", busses)
        for i in range(len(busses)):
            if busses[i] != 'x':
                self.bus_ids.append(int(busses[i]))
                self.bus_id_info_dict[int(busses[i])] = [i]
        print(self.target_time, self.bus_ids)

    def find_earliest_departure(self):
        earliest_departure = 0
        best_bus = 0
        for bus_id in self.bus_ids:
            if self.target_time % bus_id == 0:
                departure = self.target_time
                return departure, bus_id
            else:
                matched_time = bus_id * ceil(self.target_time / bus_id)
                if (earliest_departure == 0) or (matched_time < earliest_departure):
                    earliest_departure = matched_time
                    best_bus = bus_id
        return earliest_departure, best_bus

    def solve_part_1(self):
        leave_time, bus_id = self.find_earliest_departure()
        difference = leave_time - self.target_time
        return difference * bus_id

    def satisfy_constraints(self):
        # Using Chinese remainder theorem only works because every bus input is a prime number
        id_product = prod(self.bus_id_info_dict)
        x = 0
        for bus_id in self.bus_id_info_dict:
            info = self.bus_id_info_dict[bus_id]
            offset = info[0]
            ri = (bus_id - offset) % bus_id
            info.append(ri)
            ni = id_product // bus_id
            info.append([ni])
            c = ni % bus_id
            xi = 1
            while (c * xi) % bus_id != 1:
                xi += 1
            info.append(xi)
            x += ri * ni * xi
        t = x % id_product
        return t


def main():
    finder = Scheduler(instruction_file_path)
    print(finder.solve_part_1())
    print(finder.satisfy_constraints())


if __name__ == "__main__":
    main()
