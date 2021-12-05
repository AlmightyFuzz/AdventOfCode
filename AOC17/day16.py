import re
import functools

TEST_MOVES = 's1,x3/4,pe/b'
TEST_DANCERS = 'abcde'
PUZZLE_DANCERS = 'abcdefghijklmnop'


def dance_lots(dancers_str, dance_moves_str):

    for _ in range(1000000000):
        dancers_str = dance(dancers_str, dance_moves_str)

    print(dancers_str)


# Uses built in Python memoisation function to remember previously calculated results.
# This greatly speeds up computation when performing a very large number of iterations
@functools.lru_cache()
def dance(dancers_str, dance_moves_str):
    '''Computes the position of the dancers after applying the set of dance moves'''

    dancers = list(dancers_str)
    dance_moves = dance_moves_str.split(',')

    for move in dance_moves:
        if move[0] == 's':
            # Takes the last x number of chars from the end of
            # the string and puts them at the front
            spin_range = int(move[1:])
            dancers = dancers[0 - spin_range:] + \
                dancers[:0 - spin_range]
        else:
            if move[0] == 'x':
                # Using regex to handle variable number of digits
                match = re.match(r'x(?P<posA>\d+)\/(?P<posB>\d+)', move)
                pos_a = int(match.group('posA'))
                pos_b = int(match.group('posB'))

            if move[0] == 'p':
                # Program names are always one character, so no need to use regex
                pos_a = dancers.index(move[1])
                pos_b = dancers.index(move[3])

            dancers[pos_a], dancers[pos_b] = dancers[pos_b], dancers[pos_a]

    return ''.join(dancers)


def load_puzzle():
    return open('day16input.txt', 'r').readline()


if __name__ == '__main__':
    # -Part 1-
    # print(''.join(dance(list(TEST_DANCERS), TEST_MOVES)))
    # print(''.join(dance(list(PUZZLE_DANCERS), load_puzzle())))

    # -Part 2-
    dance_lots(PUZZLE_DANCERS, load_puzzle())
