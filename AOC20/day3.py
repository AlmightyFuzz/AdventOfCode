
test_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def traverse_slope(input, slope_x, slope_y):
    width = len(input[0])
    height = len(input)

    x = 0
    y = 0
    num_trees = 0

    at_bottom = False
    while not at_bottom:

        if x + slope_x >= width:
            x = (x + slope_x) - width
        else:
            x += slope_x

        if y + slope_y >= height:
            at_bottom = True
            continue
        else:
            y += slope_y

        if input[y][x] == '#':
            num_trees += 1

    return num_trees


def get_puzzle_input():
    with open('InputData/day3.txt', 'r') as file:
        file_data = [line.strip('\n') for line in file]

        return file_data


if __name__ == '__main__':
    #map = test_data.split('\n')
    map = get_puzzle_input()

    a = traverse_slope(map, slope_x=1, slope_y=1)
    b = traverse_slope(map, slope_x=3, slope_y=1)
    c = traverse_slope(map, slope_x=5, slope_y=1)
    d = traverse_slope(map, slope_x=7, slope_y=1)
    e = traverse_slope(map, slope_x=1, slope_y=2)

    print(a * b * c * d * e)
