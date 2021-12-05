TEST = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''


def parse_coords(data):
    coords = []

    for line in data:
        chunks = line.split(', ')
        x = int(chunks[0])
        y = int(chunks[1])

        coords.append((x, y))

    return set(coords)


def find_bounding_box(coords, expansion):
    # expansion value is used make the bounding box larger or smaller as needed
    bounding_box = dict()
    bounding_box['min_x'] = min([coord[0] for coord in coords]) - expansion
    bounding_box['min_y'] = min([coord[1] for coord in coords]) - expansion
    bounding_box['max_x'] = max([coord[0] for coord in coords]) + expansion
    bounding_box['max_y'] = max([coord[1] for coord in coords]) + expansion

    return bounding_box


def find_box_edges(bounding_box):
    x_range = range(bounding_box['min_x'], bounding_box['max_x'])
    y_range = range(bounding_box['min_y'], bounding_box['max_y'])

    top = set([(x, bounding_box['min_y']) for x in x_range])
    bottom = set([(x, bounding_box['max_y']) for x in x_range])
    left = set([(bounding_box['min_x'], y) for y in y_range])
    right = set([(bounding_box['max_x'], y) for y in y_range])

    return top | bottom | left | right


def find_distance(a, b):
    # Distance between a and b
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def do_the_thing(coords):
    expansion = 0
    bounding_box = find_bounding_box(coords, expansion)
    box_edges = find_box_edges(bounding_box)
    coord_area = {coord: set() for coord in coords}

    grid_coords = [(x, y)
                   for x in range(bounding_box['min_x'], bounding_box['max_x'] + 1)
                   for y in range(bounding_box['min_y'], bounding_box['max_y'] + 1)]

    for grid_coord in grid_coords:
        dist_to_coords = [(find_distance(grid_coord, coord), coord)  # (dist, coord) tuple
                          for coord in coords]

        # tuple sorts are done lexigraphically, so the coord part will only be
        # compared when the dists are equal
        dist_to_coords.sort()

        if dist_to_coords[0][0] != dist_to_coords[1][0]:
            coord = dist_to_coords[0][1]
            coord_area[coord].add(grid_coord)

    finite_areas = []
    for coord, area in coord_area.items():
        # if area does not have points along the edge (ie infinte area)
        if area.isdisjoint(box_edges):
            finite_areas.append(area)

    print('Largest area: ' + str(max([len(x) for x in finite_areas])))


def do_other_thing(coords, region_dist=10000):
    expansion = 0
    bounding_box = find_bounding_box(coords, expansion)
    safe_region = set()

    grid_coords = [(x, y)
                   for x in range(bounding_box['min_x'], bounding_box['max_x'] + 1)
                   for y in range(bounding_box['min_y'], bounding_box['max_y'] + 1)]

    for grid_coord in grid_coords:
        dist_to_coords = [find_distance(grid_coord, coord) for coord in coords]

        if sum(dist_to_coords) < region_dist:
            safe_region.add(grid_coord)

    print("Safe area size: " + str(len(safe_region)))


if __name__ == "__main__":
    # coord_data = TEST.split('\n')
    coord_data = [line.strip('\n')
                  for line in open('InputData/day6Input.txt', 'r')]

    coords = parse_coords(coord_data)
    do_other_thing(coords)
