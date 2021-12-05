TEST1 = [0, 3, 0, 1, -3]


def jump_jump_jump(maze):  # jump up and get down
    jump_num = 0
    idx = 0

    while True:
        if idx < 0 or idx >= len(maze):
            break

        # extract the jump distance
        jump = maze[idx]

        # update the existing jump value
        if jump >= 3:
            maze[idx] = jump - 1
        else:
            maze[idx] = jump + 1

        # jump to new location
        idx = idx + jump

        # count the jump
        jump_num += 1

    return jump_num


def process_puzzle_input():
    data = []
    file = open('day5input.txt', 'r')

    for line in file:
        data.append(int(line))

    print(jump_jump_jump(data))


if __name__ == "__main__":
    print(jump_jump_jump(TEST1))
    # process_puzzle_input()
