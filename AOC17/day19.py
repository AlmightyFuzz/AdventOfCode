from enum import Enum, auto

TEST = '''
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
                
'''


def packet_tracer(route_map):
    '''Follows the path traced out by the route map'''
    num_steps = 1
    locations = []
    direction = Direction.South

    # item => ((x, y), ' ')
    for item in route_map.items():
        if item[1] != ' ':
            position = item[0]
            break  # found start point

    while True:
        # Travel until we reach a Point Of Interest
        poi_data = travel(route_map, position, direction)

        poi = poi_data[0]
        num_steps += poi_data[1]

        if route_map[poi] == '+':
            direction = change_direction(route_map, poi, direction)
        else:
            locations.append(route_map[poi])

            if the_end(poi, direction, route_map):
                break

        position = poi

    print(''.join(locations), num_steps)


def travel(route_map, position, direction):
    '''Follows the route map in a given direction until it finds a point of interest.'''
    x = position[0]
    y = position[1]
    steps = 0

    while True:
        if direction == Direction.North:
            y -= 1
        elif direction == Direction.East:
            x += 1
        elif direction == Direction.South:
            y += 1
        elif direction == Direction.West:
            x -= 1

        steps += 1

        if route_map[x, y] != '|' and route_map[x, y] != '-':
            return (x, y), steps

        # Will let Not In Dict exception handle running off the edge of the map


def change_direction(route_map, position, curr_direction):
    '''Determine which new direction to travel in by looking at the four surrounding spaces.'''
    x = position[0]
    y = position[1]

    n_space = route_map[x, y - 1]
    e_space = route_map[x + 1, y]
    s_space = route_map[x, y + 1]
    w_space = route_map[x - 1, y]

    # Don't look at the space behind you
    if n_space != ' ' and curr_direction != Direction.South:
        return Direction.North

    if e_space != ' ' and curr_direction != Direction.West:
        return Direction.East

    if s_space != ' ' and curr_direction != Direction.North:
        return Direction.South

    if w_space != ' ' and curr_direction != Direction.East:
        return Direction.West


def the_end(position, direction, route_map):
    '''Determine if you've reached the end of the path'''
    x = position[0]
    y = position[1]

    if direction == Direction.North:
        next_space = route_map[x, y - 1]
    elif direction == Direction.East:
        next_space = route_map[x + 1, y]
    elif direction == Direction.South:
        next_space = route_map[x, y + 1]
    elif direction == Direction.West:
        next_space = route_map[x - 1, y]

    return next_space == ' '


def createMap(data):
    route_map = dict()

    for y, row in enumerate(data):
        for x, space in enumerate(row):
            route_map[x, y] = space

    return route_map


class Direction(Enum):
    # Note: auto() requires Python 3.6+
    North = auto()
    East = auto()
    South = auto()
    West = auto()


def load_puzzle():
    return [line.strip('\n') for line in open('day19input.txt').readlines()]


if __name__ == '__main__':
    # packet_tracer(createMap(TEST.strip('\n').split('\n')))
    packet_tracer(createMap(load_puzzle()))
