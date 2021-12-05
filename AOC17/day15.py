TEST = (65, 8921)
PUZZLE_INPUT = (699, 124)


def dual_of_the_generators(in_data, picky=None):
    if picky:
        gen_a = generator(in_data[0], 16807, 4)
        gen_b = generator(in_data[1], 48271, 8)
        iterations = 5000000
    else:
        gen_a = generator(in_data[0], 16807)
        gen_b = generator(in_data[1], 48271)
        iterations = 40000000

    num_pairs = 0
    for _ in range(iterations):
        # take the last 16 binary digits and compare them
        if bin(next(gen_a))[-16:] == bin(next(gen_b))[-16:]:
            num_pairs += 1

    print('There are {0} pairs'.format(num_pairs))


def generator(seed, factor, criteria=None):
    '''A generator to provide values as described by the puzzle'''
    prev_val = seed

    while True:
        result = (prev_val * factor) % 2147483647

        if criteria:  # picky generator
            if result % criteria == 0:
                yield result
        else:
            yield result

        prev_val = result


if __name__ == '__main__':
    # -Part 1-
    # dual_of_the_generators(TEST)
    # dual_of_the_generators(PUZZLE_INPUT)

    # -Part 2-
    # dual_of_the_generators(TEST, True)
    dual_of_the_generators(PUZZLE_INPUT, True)
