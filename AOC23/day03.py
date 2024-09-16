import common
import re

TEST_DATA = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def find_all_numbers(diagram):
    '''Finds the numbers in the engine diagram, and returns the index of the first digit of each number'''

    digit_rgx = re.compile(r"\d")
    numbers = []

    for row in range(0, len(diagram)):
        reading_number = False
        
        for column in range(0, len(diagram[0])):
            char = diagram[row][column]

            if digit_rgx.match(char):
                if not reading_number:
                    numbers.append((column,row))
                    reading_number = True
            else:
                reading_number = False

    return numbers

def check_for_part_numbers(number_indexes, diagram):
    '''Finds all numbers and checks if they are surrounded by any partnumber characters.'''
    part_num_total = 0
    part_num_rgx = re.compile(r"[^\d\.]") #not a digit or a period
    num_rgx = re.compile(r"\d+")

    for idx in number_indexes:
        num_adjacent_chars = find_number_with_adjacent_chars(idx, diagram)
        string = ''.join(num_adjacent_chars)

        if part_num_rgx.search(string):
            match = num_rgx.search(string)
            part_num_total += int(match[0])

    print(part_num_total)


def find_number_with_adjacent_chars(index, diagram):
    '''Draws a box around the number and returns the contents of the box.'''
    adjacent_chars = []
    digit_rgx = re.compile(r"\d")

    column_idx = index[0]
    row_idx = index[1]
    top_left = [0 if column_idx == 0 else column_idx - 1, 0 if row_idx == 0 else row_idx - 1]

    # find the last index of the number
    while(True):
        next_column_index = column_idx + 1
        if next_column_index >= len(diagram[0]):
            break

        next_char = diagram[row_idx][next_column_index]
                            
        if digit_rgx.match(next_char):
            column_idx = next_column_index
        else:
            break
   
    bottom_right = [column_idx if column_idx == len(diagram[0]) - 1 else column_idx + 1,
                     row_idx if row_idx == len(diagram) - 1 else row_idx + 1]
    
    for y in range(top_left[1], bottom_right[1] + 1):
        for x in range(top_left[0], bottom_right[0] + 1):
            adjacent_chars.append(diagram[y][x])

    return adjacent_chars

def find_gear_ratio_total(diagram):
    gear = '*'
    total_ratio = 0

    for row in range(0, len(diagram)):
        for column in range(0, len(diagram[0])):
            char = diagram[row][column]

            if char == gear:
                indices = get_surrouding_indices((column, row), diagram)
                numbers = find_numbers(indices, diagram)

                if len(numbers) == 2:
                    ratio = numbers[0] * numbers[1]
                    total_ratio += ratio

    print(total_ratio)


def get_surrouding_indices(index, diagram):
    (ix,iy) = index
    len_x = len(diagram[0])
    len_y = len(diagram)

    start_x = ix - 1
    end_x = ix + 1
    start_y = iy - 1
    end_y = iy + 1

    if ix <= 0:
        start_x = 0

    if ix >= len_x:
        end_x = len_x

    if iy <= 0:
        start_y = 0
    
    if iy >= len_y:
        end_y = len_y

    indices = [(x, y) for x in range(start_x, end_x + 1) for y in range(start_y, end_y + 1)]

    return indices

def find_numbers(indices, diagram):
    is_digit = re.compile(r"\d")
    numbers = []

    for index in indices:
        (x, y) = index
        char = diagram[y][x]

        if is_digit.match(char):
            num = extract_number(index, diagram)

            if num not in numbers:
                numbers.append(num)

    return numbers


def extract_number(index, diagram):
    is_digit = re.compile(r"\d")
    (x, y) = index
    char = diagram[y][x]

    if not is_digit.match(char):
        return None
    
    start_x = x
    while(True):
        c = diagram[y][start_x]

        if not is_digit.match(c):
            start_x += 1 #we've gone too far so go back one
            break
        
        if start_x == 0:
            break
        
        start_x -= 1

    end_x = x
    while(True):
        c = diagram[y][end_x]

        if not is_digit.match(c):
            end_x -= 1 #we've gone too far so go back one
            break
        
        if end_x == len(diagram[0]) - 1:
            break

        end_x += 1

    num_str = ""
    for i in range(start_x, end_x + 1):
        num_str += diagram[y][i]

    return int(num_str)


if __name__ == "__main__":
    #puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day03.txt")

    # part 1
    #nums = find_all_numbers(puz_input)
    #check_for_part_numbers(nums, puz_input)

    # part 2
    find_gear_ratio_total(puz_input)