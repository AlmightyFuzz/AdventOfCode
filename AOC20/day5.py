test_data1 = "BFFFBBFRRR" #row 70, column 7, seat ID 567
test_data2 = "FFFBBBFRRR" #row 14, column 7, seat ID 119
test_data3 = "BBFFBBFRLL" #row 102, column 4, seat ID 820

def get_puzzle_input():
    with open("InputData/day5.txt") as file:
        return [line.strip('\n') for line in file]

def read_boardingpass(b_pass):
    row_values = list(range(0,128))
    row_steps = b_pass[:7]
    col_values = list(range(0,8))
    col_steps = b_pass[-3:]

    row = calculate_value(row_steps, row_values)
    col = calculate_value(col_steps, col_values)

    return row * 8 + col


def calculate_value(steps, values):
    if len(values) <= 1:
        return values[0]

    step = steps[0]
    mid_index = int(len(values)/2)

    if step in {'F', 'L'}:
        return calculate_value(steps[1:], values[:mid_index])
    elif step in {'B', 'R'}:
        return calculate_value(steps[1:], values[mid_index:])


def find_highest_id(boarding_passes):
    largest_val = 0
    
    for b_pass in boarding_passes:
        seat_id = read_boardingpass(b_pass)

        if seat_id > largest_val:
            largest_val = seat_id

    return largest_val

def find_missing_id(boarding_passes):
    ids = [read_boardingpass(b) for b in boarding_passes]
    ids.sort()

    # all ids are present and consecutive, except one
    for i in range(0, len(ids)):
        if ids[i] != ids[i+1] - 1:
            return ids[i] + 1

if __name__ == "__main__":
    #print(read_boardingpass(test_data1))
    #print(read_boardingpass(test_data2))
    #print(read_boardingpass(test_data3))

    input = get_puzzle_input()
    #print(find_highest_id(input))

    missing_id = find_missing_id(input)
    print(missing_id)