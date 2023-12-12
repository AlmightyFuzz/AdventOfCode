TEST1 = """5 1 9 5
7 5 3
2 4 6 8"""

TEST2 = """5 9 2 8
9 4 7 3
3 8 6 5"""

PUZZLE_INPUT = """"""


def convert_data_to_table(in_str):
    # Turn data into a list of rows
    list_of_rows = in_str.split('\n')

    # Convert each row into list of ints, then add that list to an overall list
    table = []
    for row in list_of_rows:
        if ' ' in row:
            tmp = row.split(' ')
            int_list = []

            for i in tmp:
                int_list.append(int(i))

            table.append(int_list)

        elif '\t' in row:
            tmp = row.split('\t')
            int_list = []

            for i in tmp:
                int_list.append(int(i))

            table.append(int_list)

    return table


def find_max_and_min(in_list):
    max_val = max(in_list)
    min_val = min(in_list)

    return (max_val, min_val)


def find_divisable_nums(in_list):
    a = 0
    b = 0

    # Foreach item in list
    for i in range(len(in_list)):
        x = in_list[i]

        # Foreach item the rest of the list
        for j in in_list[i + 1:]:
            # Check if nums divide into each other neatly
            if x % j == 0:
                a = x
                b = j
            elif j % x == 0:
                a = j
                b = x

    return (a, b)


def checksum(in_data):
    table = convert_data_to_table(in_data)

    # Apply findMaxAndMin function to each element (ie row) in table
    max_and_mins = list(map(find_max_and_min, table))

    total = 0
    for tpl in max_and_mins:
        total += int(tpl[0]) - int(tpl[1])

    return total


def checksum2(in_data):
    total = 0

    table = convert_data_to_table(in_data)

    for row in table:
        tpl = find_divisable_nums(row)

        if tpl[0] == 0 or tpl[1] == 0:
            total += 0
        else:
            total += int(tpl[0]) // int(tpl[1])

    return total


if __name__ == '__main__':
    # print(checksum(TEST1))
    print(checksum2(TEST2))

    # print(checksum(puzzleInput))
    print(checksum2(PUZZLE_INPUT))
