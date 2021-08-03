seats = '/home/ryan/Documents/AdventOfCode/2020/Day11/seating_chart.txt'
# seats = '/home/ryan/Documents/AdventOfCode/2020/Day11/test_seats.txt'


class Seater:
    def __init__(self, file_path):
        self.file_path = file_path
        self.deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.num_rows = 0
        self.num_cols = 0
        self.seating_limit = 0

    def make_initial_seating_chart(self):
        with open(self.file_path, "r") as f:
            lines = [line.rstrip() for line in f.readlines()]
            lines = [list(line) for line in lines]
        return lines

    def count_occupied(self, row_index, column_index, seating_chart):
        count = 0
        self.num_rows = len(seating_chart)
        self.num_cols = len(seating_chart)
        for i, j in self.deltas:
            xi, xj = row_index + i, column_index + j
            if 0 <= xi < self.num_rows and 0 <= xj < self.num_cols and seating_chart[xi][xj] == '#':
                count += 1
        return count

    def check_occupied(self, seat_tolerance, part):
        count = 0
        self.seating_limit = seat_tolerance
        seating_chart = self.make_initial_seating_chart()
        while True:
            valid = True
            temp_seating = [r.copy() for r in seating_chart]
            for i, r in enumerate(temp_seating):
                for j, c in enumerate(r):
                    if part == 1:
                        count = self.count_occupied(i, j, temp_seating)
                    if part == 2:
                        count = self.count_occupied_2(i, j, temp_seating)
                    if c == 'L' and count == 0:
                        seating_chart[i][j] = '#'
                    elif c == '#' and count >= self.seating_limit:
                        seating_chart[i][j] = 'L'
                    valid &= (r[j] == seating_chart[i][j])
            if valid:
                break
        answer = 0
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if seating_chart[i][j] == '#':
                    answer += 1
        print(f"There are {answer} valid seats.")

    def count_occupied_2(self, row_index, column_index, seating_chart):
        count = 0
        self.num_rows = len(seating_chart)
        self.num_cols = len(seating_chart)
        for i, j in self.deltas:
            xi, xj = row_index + i, column_index + j
            while 0 <= xi < self.num_rows and 0 <= xj < self.num_cols:
                if seating_chart[xi][xj] == '#':
                    count += 1
                    break
                elif seating_chart[xi][xj] == 'L':
                    break
                xi += i
                xj += j
        return count


def main():
    seat_counter = Seater(seats)
    seat_counter.check_occupied(4, 1)
    seat_counter.check_occupied(5, 2)


if __name__ == "__main__":
    main()
