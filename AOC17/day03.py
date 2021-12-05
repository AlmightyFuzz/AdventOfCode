'''
The program works by keeping track of the current position in the spiral
memory sequence as a 2D point relative to the start point, and also keeps
track of the direction of travel and at which values to change direction.
It then just steps through the until it reaches the destination valuem,
at which point it uses its 2D point to work out the distance back to the start
'''
from enum import Enum, auto

PUZZLE_INPUT = 325489
TEST1 = 1  # 0
TEST2 = 12  # 3
TEST3 = 23  # 2
TEST4 = 1024  # 31


def spiral_memory(target_num):
    # Start at value of 1, represented as [0,0], with starting direction being
    # South so that it turns to face the correct direction at the start.
    direc = Direction.South
    point = Point(0, 0)
    count = 1

    cell_value = 0
    spiral_data = {}

    # Initialise the first turning number
    turning_num_gen = get_next_turning_num()
    turning_num = next(turning_num_gen)

    while count <= target_num:

        if count == 1:
            point.X, point.Y = 0, 0
        else:
            if direc == Direction.East:
                point.X += 1
            elif direc == Direction.North:
                point.Y += 1
            elif direc == Direction.West:
                point.X -= 1
            elif direc == Direction.South:
                point.Y -= 1

        if count == turning_num:
            direc = change_direction(direc)
            turning_num = next(turning_num_gen)

        if count == 1:
            cell_value = 1
        else:
            cell_value = find_cell_value(point, spiral_data)

        # str(Point(xVal,yVal)) converts the point to the string '[xVal,yVal]'
        spiral_data[str(point)] = cell_value

        count += 1

        # Part 2
        if cell_value > target_num:
            print('Value:', cell_value)
            break

    steps = abs(point.X) + abs(point.Y)

    return steps


def find_cell_value(point, spiral_data):
    '''
    Check the 8 adjacent cells for their values. If there is no value for that cell
    then just carry on to the next. So long as this done for each cell as you work
    your way around the spiral then it should find the correct values, as the blank
    adjacent cells are just ones we haven't reached yet and therefore dont care about
    '''
    new_cell_value = 0
    other_point = Point(point.X, point.Y)

    for i in range(8):
        if i == 0:
            other_point.X += 1
        elif i == 1:
            other_point.Y -= 1
        elif i in [2, 3]:
            other_point.X -= 1
        elif i in [4, 5]:
            other_point.Y += 1
        elif i in [6, 7]:
            other_point.X += 1

        if str(other_point) in spiral_data:
            new_cell_value += spiral_data[str(other_point)]

    return new_cell_value


def change_direction(direction):
    '''
    Turns anti-clockwise
    '''

    if direction == Direction.North:
        return Direction.West
    elif direction == Direction.West:
        return Direction.South
    elif direction == Direction.South:
        return Direction.East
    elif direction == Direction.East:
        return Direction.North


def get_next_turning_num():
    '''
    The 'turning numbers' (ie, where the direction of travel changes)
    are 1,2,3,5,7,10,13,17,etc. The generator produces that sequence of numbers
    The differnce betweeen the those numbers
    are 1,1,2,2,3,3,4,etc which the generator() generator produces.
    '''
    next_num = 1
    gen = generator()

    while True:
        yield next_num

        next_num += next(gen)


def generator():
    '''Generates the sequence 1,1,2,2,3,3,4,4,5,5 etc'''
    num = 1
    flip_flop = False

    while True:
        yield num

        if flip_flop is True:
            num += 1
            flip_flop = False
        else:
            flip_flop = True


class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return '[{0},{1}]'.format(self.X, self.Y)


class Direction(Enum):
    # Note auto() requires Python 3.6+
    North = auto()
    East = auto()
    South = auto()
    West = auto()


if __name__ == '__main__':
    # print(SpiralMemory(TEST1)) #0
    # print(SpiralMemory(TEST2)) #3
    # print(SpiralMemory(TEST3)) #2
    # print(SpiralMemory(TEST4)) #31

    print(spiral_memory(PUZZLE_INPUT))
