import common

TEST_DATA = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def find_char_points(grid, char):
    x_points = []
    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == char:
                x_points.append((x, y))

    return x_points


def turn_gaurd(direction):
    match direction:
        case "n":
            return "e"
        case "e":
            return "s"
        case "s":
            return "w"
        case "w":
            return "n"


def next_step(point, direction):
    x, y = point

    match direction:
        case "n":
            return (x, y - 1)
        case "e":
            return (x + 1, y)
        case "s":
            return (x, y + 1)
        case "w":
            return (x - 1, y)


def is_outside_grid(point, grid):
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    x, y = point

    return x < 0 or x > max_x or y < 0 or y > max_y


def plot_walk(grid):
    guard_point = find_char_points(grid, "^")
    obstacles = find_char_points(grid, "#")
    guard_dir = "n"

    current_point = guard_point[0]
    positions = []
    # positions.add(current_point)

    left_grid = False

    while not left_grid:
        # print(current_point)
        positions.append(current_point)

        next_point = next_step(current_point, guard_dir)

        if next_point in obstacles:
            guard_dir = turn_gaurd(guard_dir)
        elif is_outside_grid(next_point, grid):
            left_grid = True
        else:
            current_point = next_point

    unique_posititions = set(positions)
    print("unique positions: " + str(len(unique_posititions)))


if __name__ == "__main__":
    # puz_input = common.load_test_data(TEST_DATA)
    # answer is one less than correct answer
    puz_input = common.load_puzzle_input("data/day06.txt")

    plot_walk(puz_input)
