import math

TEST = '''
../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
'''


def programmer_art(rules_data):
    rules = {rule[0].replace('/', ''): rule[1].replace('/', '')
             for rule in (line.split(' => ') for line in rules_data)}

    grid = ['.#...####']
    print(grid)

    for _ in range(2):

        for sub_grid in grid:
            grid = process_grid(grid, rules)

        copy = list(grid)  # replace original grid with new split
        for i, sub_grid in enumerate(grid):
            if len(sub_grid) == 16:
                ls = []

                # grid[i] =


def process_grid(grid_inp, the_rules):
    if len(grid_inp) == 4:
        grid_inp = [grid_inp[:2], grid_inp[2:]]
    elif len(grid_inp) == 9:
        grid_inp = [grid_inp[:3], grid_inp[3:6], grid_inp[6:]]

    perms = permutations(grid_inp)

    for perm in perms:
        flat_grid = ''.join(row for row in perm)

        # check if there is a rule that matches the current grid pattern
        if flat_grid in the_rules.keys():
            return the_rules[flat_grid]


def permutations(grid_inp):
    # @functools.lru_cache()
    # use memoisation to return previously seen results?

    perms = [grid_inp]

    rotate = grid_inp
    for _ in range(3):  # get 90, 180, and 270 degree rotations
        rotate = rotate_90(rotate)
        perms.append(rotate)

    flipped = list(map(flip, perms))

    perms += flipped

    return perms  # needs to be hashable for the memoisation


def rotate_90(array2d):
    '''Rotate a square 2D array by 90 degrees clockwise'''

    # array2d = [[123],[456],[789]]
    #
    # The 'zip(*array2d[::-1])' expression works by reversing the outer list with 'array2d[::-1]' ([[789],[456],[123]]),
    # and then unpacking each element in that list ('*') before giving it to zip ( zip([789],[456],[123]) ).
    # Zip then makes in iterator that returns the first elements of *each* list, then the second elements, then the third
    # etc ([[741],[852],[963]])
    #
    # 123    741
    # 456 => 852
    # 789    963

    rot = zip(*array2d[::-1])  # voodoo magic

    return [''.join(i) for i in rot]


def flip(array2d):
    '''Flips a square 2D array along the vertical axis'''
    # Flipping in the horizontal axis is just the same as rotating 180 degrees.

    return [line[::-1] for line in array2d]


def split_array(array2d):
    # It's ugly and brittle but it works for now
    if len(array2d) == 4:
        return [[array2d[0][:2], array2d[1][:2]],
                [array2d[0][2:], array2d[1][2:]],
                [array2d[2][:2], array2d[3][:2]],
                [array2d[2][2:], array2d[3][2:]]]

    if len(array2d) == 6:
        split = [[array2d[0][:3], array2d[1][:3], array2d[2][:3]],
                 [array2d[0][3:], array2d[1][3:], array2d[2][3:]],
                 [array2d[3][:3], array2d[4][:3], array2d[5][:3]],
                 [array2d[3][3:], array2d[4][3:], array2d[5][3:]]]

        for i in split:
            print(i)

        return split


if __name__ == '__main__':
    programmer_art(TEST.strip('\n').split('\n'))
