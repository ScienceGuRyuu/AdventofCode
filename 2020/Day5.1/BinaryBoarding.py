from operator import add
passes_file_path = "PATH_TO_FILE"

with open(passes_file_path) as file:
    passes_list = [line.strip() for line in file]

passes_list_binary_1 = [letter.replace("B", '1') for letter in passes_list] 
passes_list_binary_2 = [letter.replace("F", '0') for letter in passes_list_binary_1] 
passes_list_binary_3 = [letter.replace("L", '0') for letter in passes_list_binary_2] 
passes_list_binary_4 = [letter.replace("R", '1') for letter in passes_list_binary_3] 

row = [i[:7] for i in passes_list_binary_4]
row_decimal = [int(i, 2) for i in row]
row_decimal_times_8 = [i * 8 for i in row_decimal]
column = [i[7:] for i in passes_list_binary_4]
column_decimal = [int(i, 2) for i in column]

seat_ids = list(map(add, row_decimal_times_8, column_decimal))
seat_ids.sort()
seat_ids.reverse()
print(seat_ids[0])

for i in range(0, len(seat_ids)):
    if i != 0 or i != (len(seat_ids) - 1):
        if (seat_ids[i] - 1 ) not in seat_ids and (seat_ids[i] - 2) in seat_ids: and 
            print (seat_ids[i]-1)

        

