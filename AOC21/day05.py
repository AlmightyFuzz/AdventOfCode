import common
from itertools import product

TEST_DATA = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def process_data(data):
    line_segments = [[tuple([int(val) for val in coord.split(',')])
                      for coord in line.split(" -> ")]
                     for line in data]

    return line_segments


def find_larget_x_and_y(lines):
    largest_x = 0
    largest_y = 0

    for line in lines:
        xs = [coord[0] for coord in line]
        ys = [coord[1] for coord in line]

        if max(xs) > largest_x:
            largest_x = xs[0]

        if max(ys) > largest_y:
            largest_y = ys[0]

    return (largest_x, largest_y)


def initial_vent_map(x, y):
    coords = product(range(x+1), range(y+1))

    blank_map = {coord: 0 for coord in coords}

    return blank_map

def enumerate_values(a, b):
    """Returns the values between a and b inclusively, in increasing or decreasing order depending."""
    values = []

    if a <= b:
        # increasing
        values = list(range(a, b+1))
    elif a > b:
        # decreasing
        values = list(range(a, b-1, -1))

    return values

def fill_vent_map(vent_map, lines, straight_lines_only=False):
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]

        coords = []
        xs = enumerate_values(x1, x2)
        ys = enumerate_values(y1, y2)
        
        if x1 == x2 or y1 == y2:
            # extend the short list to same length as longer list
            if len(xs) == 1:
                xs = [xs[0]] * len(ys)
            elif len(ys) == 1:
                ys = [ys[0]] * len(xs)
        else: # diagonal line
            if straight_lines_only:
                continue

        coords = [x for x in zip(xs, ys)]

        for coord in coords:
            vent_map[coord] += 1

    return vent_map


if __name__ == "__main__":
    #data = common.load_test_data(TEST_DATA)
    data = common.load_puzzle_input("data/day05.txt")
    lines = process_data(data)

    lx, ly = find_larget_x_and_y(lines)
    vent_map = initial_vent_map(lx, ly)

    #fill_vent_map(vent_map, lines, straight_lines_only=True) # pt1
    fill_vent_map(vent_map, lines) # pt2

    danger_zones = 0
    for space in vent_map.values():
        if space >= 2:
            danger_zones += 1

    print(f"Danger zones: {danger_zones}")
