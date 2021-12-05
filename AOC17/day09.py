TEST1 = '<{!>}>'
TEST2 = '{{<!>},{<!>},{<!>},{<a>}}'  # 2 groups
TEST3 = '{{},{}}'  # 3 groups. score 5
TEST4 = '{{{}}}'  # 3 groups, score 6
TEST5 = '{<{},{},{{}}>}'  # 1 group, score 1


def read_stream(stream):
    score = 0
    score_lvl = 0
    skip_char = False
    in_garbage = False

    num_garbage_chars = 0

    for char in stream:
        # Handle cancels
        if skip_char:
            skip_char = False
            continue

        if char == '!':
            skip_char = True
            continue

        # Handle garbage
        if in_garbage:
            if char == '>':
                in_garbage = False
            else:
                num_garbage_chars += 1
                continue

        if char == '<':
            in_garbage = True

        # Handle groups and scoring
        if char == '{':
            score_lvl += 1

        if char == '}':
            score += score_lvl
            score_lvl -= 1

    print(score, num_garbage_chars)


def load_puzzle():
    f = open('day9input.txt', 'r')

    # input is just one line with no '\n', so read the whole thing
    return f.readline()


if __name__ == '__main__':
    # read_stream(TEST5)

    read_stream(load_puzzle())
