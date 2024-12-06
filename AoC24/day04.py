import common

TEST_DATA = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def find_xs(grid):
    x_points = []
    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == "X":
                x_points.append((x, y))

    return x_points


def get_surrounding_points(point, max_x, max_y):
    points = []
    x, y = point

    if y > 0:
        if x > 0:
            points.append(((x - 1, y - 1), "nw"))

        points.append(((x, y - 1), "n"))

        if x < max_x:
            points.append(((x + 1, y - 1), "ne"))

    if x > 0:
        points.append(((x - 1, y), "w"))

    if x < max_x:
        points.append(((x + 1, y), "e"))

    if y < max_y:
        if x > 0:
            points.append(((x - 1, y + 1), "sw"))

        points.append(((x, y + 1), "s"))

        if x < max_x:
            points.append(((x + 1, y + 1), "se"))

    return points


def get_next_point(point, cardinality, max_x, max_y):
    x, y = point

    match cardinality:
        case "n":
            if y > 0:
                return (x, y - 1)
        case "ne":
            if x < max_x and y > 0:
                return (x + 1, y - 1)
        case "e":
            if x < max_x:
                return (x + 1, y)
        case "se":
            if x < max_x and y < max_y:
                return (x + 1, y + 1)
        case "s":
            if y < max_y:
                return (x, y + 1)
        case "sw":
            if x > 0 and y < max_y:
                return (x - 1, y + 1)
        case "w":
            if x > 0:
                return (x - 1, y)
        case "nw":
            if x > 0 and y > 0:
                return (x - 1, y - 1)


def find_xmas(grid):
    xmas_count = 0

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    x_points = find_xs(grid)

    for x_point in x_points:
        surrounding_points = get_surrounding_points(x_point, max_x, max_y)

        for s_point in surrounding_points:
            point = s_point[0]
            cardinality = s_point[1]
            c = grid[point[1]][point[0]]

            if c == "M":
                next_point = get_next_point(point, cardinality, max_x, max_y)

                if next_point is not None:
                    c = grid[next_point[1]][next_point[0]]

                    if c == "A":
                        next_point = get_next_point(
                            next_point, cardinality, max_x, max_y
                        )

                        if next_point is not None:
                            c = grid[next_point[1]][next_point[0]]

                            if c == "S":
                                xmas_count += 1

    print("XMAS count: " + str(xmas_count))


if __name__ == "__main__":
    # puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day04.txt")

    find_xmas(puz_input)
