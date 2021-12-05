import re

TEST1 = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""


def build_program_map():
    program_data = load_test_input(TEST1)
    #program_data = load_puzzle_input()

    program_list = process_data(program_data)

    # find all the programs that are holding up other programs
    supporting_progs = [prog for prog in program_list if prog.holding_up != []]

    # foreach program that is holding up another,
    for s_prog in supporting_progs:
        # get the names of those other programs,
        for i, supported_prog_name in enumerate(s_prog.holding_up):
            # find the relevant program in the programList,
            for main_prog in program_list:
                # then link those programs together
                if supported_prog_name == main_prog.name:
                    main_prog.stood_on = s_prog
                    s_prog.holding_up[i] = main_prog

    return program_list


def balance_towers(program_map):
    '''Finds the programs whose weights don't balance'''

    for prog in program_map:
        if prog.stood_on is None:
            base_prog = prog
            print('Base: ', base_prog.name)

    calculate_weights(base_prog)

    unbalanced_progs = []

    for p in program_map:
        if p.holding_up != []:
            weight = p.holding_up[0].total_weight

            for i in p.holding_up:
                if i.total_weight != weight:
                    unbalanced_progs.append(p)
                    break

    for p in unbalanced_progs:
        for i in p.holding_up:
            print(p.name + '\t', i.name, ':' + str(i.total_weight) +
                  ':', str(i.weight), str(i.carried_weight))

        print()

    # You'll have to work out the answer from here on yourself by looking at the output


def calculate_weights(program):
    '''Runs through the linked programs and calculates all their weights'''
    if program.holding_up == []:
        return program.weight
    else:
        cw = 0
        for prog in program.holding_up:
            cw += calculate_weights(prog)

        program.carried_weight = cw

        return program.total_weight


def process_data(program_data):
    '''Reads in the data and creates the program objects from that'''
    program_list = []

    regex = r'(?P<name>[a-z]+)\s\((?P<weight>\d+)\)( -> (?P<progList>.*))?'

    for item in program_data:
        match = re.match(regex, item)
        if not match:
            print('No Match found')
            continue

        prog = Program(match.group('name'))
        prog.weight = int(match.group('weight'))
        if match.group('progList'):
            prog_list = match.group('progList')
            prog_list = prog_list.replace(' ', '')
            prog_list = prog_list.split(',')

            prog.holding_up = list(prog_list)

        program_list.append(prog)

    return program_list


def load_test_input(in_data):
    in_data = in_data.strip('\n')
    in_data = in_data.split('\n')

    return in_data


def load_puzzle_input():
    file = open('day7input.txt', 'r')

    file_data = [line.strip('\n') for line in file]

    return file_data


class Program():
    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.carried_weight = 0
        self.stood_on = None  # The program that this one is stood on
        self.holding_up = []  # The list of programs that this one is holding up

    @property
    def total_weight(self):
        return self.weight + self.carried_weight

    def __str__(self):
        return self.name


if __name__ == '__main__':
    program_map = build_program_map()

    balance_towers(program_map)
