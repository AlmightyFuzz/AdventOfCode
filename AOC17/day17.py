TEST = 3
PUZZLE_INPUT = 363


def spinlock(in_steps):
    buffer = [0]
    pos = 0

    for i in range(1, 2018):
        pos = (pos + in_steps) % len(buffer)
        buffer.insert(pos + 1, i)
        pos += 1

    print(buffer[buffer.index(2017) + 1])


# I got a lot of help from the AoC reddit for this one
def spinlock2(in_steps):

    # We are only concerned with the value of the second entry in the list as the
    # first entry will always be 0. As such we only need to check if the position
    # at each 'insert' is 0 and then keep track of what the value to be inseted at
    # position 1 will be.
    pos = 0
    second_val = 0

    for i in range(1, 50000001):
        pos = (pos + in_steps) % i

        if pos == 0:
            second_val = i

        pos += 1

    print(second_val)


if __name__ == '__main__':
    # spinlock(TEST)
    # spinlock(PUZZLE_INPUT)

    spinlock2(PUZZLE_INPUT)
