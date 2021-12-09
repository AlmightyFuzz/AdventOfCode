import common
from itertools import product

TEST_DATA = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def parse_input(data):
    heights = [[int(h) for h in line]
               for line in data]

    return heights


def get_adjacent_points(point, height_map):
    adjacent = []
    map_height = len(height_map) - 1
    map_width = len(height_map[0]) - 1
    x, y = point

    if x > 0:  # west
        adjacent.append((x-1, y))
    if x < map_width:  # east
        adjacent.append((x+1, y))
    if y > 0:  # north
        adjacent.append((x, y-1))
    if y < map_height:  # south
        adjacent.append((x, y+1))

    return adjacent


def find_lowest_points(height_map):
    lowest_points = []
    map_height = len(height_map)
    map_width = len(height_map[0])

    points = [p for p in product(range(map_width), range(map_height))]  # ??

    for point in points:
        x, y = point

        current = height_map[y][x]
        adjacent_points = get_adjacent_points(point, height_map)
        adjacent_heights = [height_map[y][x] for x, y in adjacent_points]

        if current < min(adjacent_heights):
            lowest_points.append(point)

    return lowest_points


def find_basins(lowest_points, height_map):
    basin_sizes = []

    for nadir in lowest_points:
        basin_points = []
        points_to_check = [nadir]
        known_boundaries = []

        while len(points_to_check) > 0:
            current_point = points_to_check.pop(0)
            x, y = current_point

            if height_map[y][x] < 9:
                basin_points.append(current_point)
                adjacent_points = get_adjacent_points(current_point, height_map)

                for point in adjacent_points:
                    if (point not in basin_points) and (point not in points_to_check) and (point not in known_boundaries):
                        points_to_check.append(point)
            else:
                known_boundaries.append(current_point)

        basin_points.sort()
        basin_sizes.append(len(basin_points))

    basin_sizes.sort(reverse=True)
    print(f"Result: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")


if __name__ == "__main__":
    #data = common.load_test_data(TEST_DATA)
    data = common.load_puzzle_input("data/day09.txt")

    height_map = parse_input(data)

    lowest_points = find_lowest_points(height_map)

    lowest_heights = [height_map[y][x] for x, y in lowest_points]
    risk_level = sum(lowest_heights) + len(lowest_heights)  # pt1
    print(f"Risk level: {risk_level}")

    find_basins(lowest_points, height_map)
