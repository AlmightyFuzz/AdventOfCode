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


def find_char_points(grid, char):
    x_points = []
    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == char:
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

    x_points = find_char_points(grid, "X")

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


def find_x_mas(grid):
    x_mas_count = 0
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    a_points = find_char_points(grid, "A")
    filtered_points = filter(
        lambda point: (point[0] > 0 and point[0] < max_x)
        and (point[1] > 0 and point[1] < max_y),
        a_points,
    )  # filter out the A's on the outer edge of the grid

    for a_point in filtered_points:
        x, y = a_point

        top_left = grid[y - 1][x - 1]
        top_right = grid[y - 1][x + 1]
        bottom_left = grid[y + 1][x - 1]
        bottom_right = grid[y + 1][x + 1]

        # 'MAS' diagonal down right
        if top_left == "M" and bottom_right == "S":
            if (top_right == "M" and bottom_left == "S") or (
                bottom_left == "M" and top_right == "S"
            ):
                x_mas_count += 1
        # 'MAS' diagonal down left
        elif top_right == "M" and bottom_left == "S":
            if (top_left == "M" and bottom_right == "S") or (
                bottom_right == "M" and top_left == "S"
            ):
                x_mas_count += 1
        # 'MAS' diagonal up left
        elif bottom_right == "M" and top_left == "S":
            if (bottom_left == "M" and top_right == "S") or (
                top_right == "M" and bottom_left == "S"
            ):
                x_mas_count += 1
        # 'MAS' diagonal up right
        elif top_right == "M" and top_right == "S":
            if (top_left == "M" and bottom_right == "S") or (
                bottom_right == "M" and top_left == "S"
            ):
                x_mas_count += 1

    print("X-MAS count: " + str(x_mas_count))


if __name__ == "__main__":
    # puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day04.txt")

    find_x_mas(puz_input)
