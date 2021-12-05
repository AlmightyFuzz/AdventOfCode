TEST1 = 'ne,ne,ne'  # 3
TEST2 = 'ne,ne,sw,sw'  # 0
TEST3 = 'ne,ne,s,s'  # 2
TEST4 = 'se,sw,se,sw,sw'  # 3
TEST5 = 'n,se,sw'  # 0

#   \  n  /
# nw +---+ ne
#   /     \
# -+       +-
#   \     /
# sw +---+ se
#   /  s  \


def hex_steps(path):
    point = Point(0, 0)
    furthest_steps = 0
    current_steps = 0

    steps = path.split(',')

    # N - S is the y-axis
    # NW - SE is the x-axis
    # NE - SW crosses both axes
    for step in steps:
        if step == 'n':
            point.y += 1
        elif step == 's':
            point.y -= 1
        elif step == 'se':
            point.x += 1
        elif step == 'nw':
            point.x -= 1
        elif step == 'ne':
            point.x += 1
            point.y += 1
        elif step == 'sw':
            point.x -= 1
            point.y -= 1

        current_steps = max(abs(point.x), abs(point.y))

        if current_steps > furthest_steps:
            furthest_steps = current_steps

    print('Steps: ', str(current_steps))
    print('Furthest distance: ', str(furthest_steps))


def load_file():
    f = open('day11input.txt')

    return f.readline().strip('\n')


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '[{0},{1}]'.format(self.x, self.y)


if __name__ == '__main__':
    # hex_steps(TEST1)
    # hex_steps(TEST5)
    # hex_steps(TEST2)
    # hex_steps(TEST3)
    # hex_steps(TEST4)

    hex_steps(load_file())
