import common


TEST_DATA = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def process_commands(data):
    commands = [tuple(x.split(' ')) for x in data]
    return commands

def plot_simple_course(commands):
    # Answer for Part 1
    depth = 0
    forward_pos = 0

    for cmd in commands:
        direction = cmd[0]
        distance = int(cmd[1])

        if direction == "forward":
            forward_pos += distance
        elif direction == "up":
            depth -= distance
        elif direction == "down":
            depth += distance

    print("Horizontal: ", forward_pos, " Depth: ", depth, " Result: ", depth * forward_pos)

def plot_correct_course(commands):
    # answer for Part 2
    depth = 0
    forward_pos = 0
    aim = 0

    for cmd in commands:
        direction = cmd[0]
        amount = int(cmd[1])

        if direction == "forward":
            forward_pos += amount
            depth += amount * aim
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount

    print("Horizontal: ", forward_pos, " Depth: ", depth, " Result: ", depth * forward_pos)

if __name__ == "__main__":
    #data = common.load_test_data(TEST_DATA)
    data = common.load_puzzle_input("data/day02.txt")

    commands = process_commands(data)
    
    #plot_simple_course(commands) 
    plot_correct_course(commands)
