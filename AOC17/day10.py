PUZZLE_LIST = [x for x in range(256)]  # [0 -> 255]
PUZZLE_LENGTHS = '120,93,0,90,5,80,129,74,1,165,204,255,254,2,50,113'
TEST_LIST = [x for x in range(5)]  # [0 -> 4]
TEST_LENGTHS = '3,4,1,5'


def knot_hash(run=None):
    '''Simple knot hash that returns the product of the first two elements in the circle'''

    if run == 'test':
        circle = list(TEST_LIST)
        lengths = [int(x) for x in TEST_LENGTHS.split(',')]
    else:
        circle = list(PUZZLE_LIST)
        lengths = [int(x) for x in PUZZLE_LENGTHS.split(',')]

    curr_pos = 0
    skip_size = 0

    circle_len = len(circle)

    for length in lengths:

        # -Get twisted list-
        if (curr_pos + length) >= circle_len:
            # if we're going to go past the end of the list then manually pull out the relevant
            # values, jump to the start and then carry on

            twist_list = []
            for i in range(length):
                pos = curr_pos + i

                if pos >= circle_len:
                    pos = pos - circle_len

                twist_list.append(circle[pos])
        else:
            # otherwise just slice the list
            twist_list = circle[curr_pos: curr_pos + length]

        twist_list.reverse()

        # -Update circle list with new twisted values-
        for i, num in enumerate(twist_list):
            pos = curr_pos + i

            if pos >= circle_len:
                pos = pos - circle_len

            circle[pos] = num

        # -Update position in circle-
        curr_pos += (length + skip_size)
        if curr_pos >= circle_len:
            curr_pos = curr_pos - circle_len

        skip_size += 1

    print('Hash is: ', circle[0] * circle[1])


def knot_hash2(in_str):
    '''Complex hash that returns the final hash in hex format'''

    circle = list(PUZZLE_LIST)

    # Creates a list of ASCII values for the given string, then appends the suffix values
    lengths_ascii = [ord(ch) for ch in in_str]
    lengths_ascii += [17, 31, 73, 47, 23]

    curr_pos = 0
    skip_size = 0

    circle_len = len(circle)

    for x in range(64):
        for length in lengths_ascii:

            # -Get twisted list-
            if (curr_pos + length) >= circle_len:
                # if we're going to go past the end of the list then manually pull out the relevant
                # values, jump to the start and then carry on

                twist_list = []
                for i in range(length):
                    pos = curr_pos + i

                    if pos >= circle_len:
                        # set the pos to the modulo result
                        pos = pos % circle_len

                    twist_list.append(circle[pos])
            else:
                # otherwise just slice the list
                twist_list = circle[curr_pos: curr_pos + length]

            twist_list.reverse()

            # -Update circle list with new twisted values-
            for i, num in enumerate(twist_list):
                pos = curr_pos + i

                if pos >= circle_len:
                    # set the pos to the modulo result
                    pos = pos % circle_len

                circle[pos] = num

            # -Update position in circle-
            curr_pos += (length + skip_size)
            if curr_pos >= circle_len:
                curr_pos = curr_pos % circle_len

            skip_size += 1

    # Splits the circle list into 16 different lists, each 16 elements long
    blocks = [circle[16 * i: (16 * i) + 16] for i in range(16)]

    # Bitwise XOR each element in each block and add the result to dense_hash
    dense_hash = []
    for block in blocks:
        result = 0
        for i in block:
            result ^= i  # a = a^i -> result = 34 ^ 2 ^ 89 ^ 5...

        dense_hash.append(result)

    # Convert each element in the dense_hash to its 2 digit hex value and concat them together
    hash_str = ''
    for i in dense_hash:
        hex_val = format(i, 'x')  # Converts i into hex without the '0x' prefix
        if len(hex_val) == 1:
            hash_str += '0' + hex_val
        else:
            hash_str += hex_val

    return hash_str


if __name__ == '__main__':
    # knot_hash('test')
    # knot_hash()

    # knot_hash2('')
    # knot_hash2('AoC 2017')
    # knot_hash2('1,2,3')
    # knot_hash2('1,2,4')
    print(knot_hash2(PUZZLE_LENGTHS))
