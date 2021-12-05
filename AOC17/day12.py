import re

TEST = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""


def digital_plumber(programs_list):
    regex = r'(?P<prog_id>\d+) <-> (?P<prog_list>.*)'
    programs = dict()

    # -Read data and populate dictionary-
    for program_str in programs_list:
        match = re.match(regex, program_str)
        prog_id = int(match.group('prog_id'))
        prog_list = [int(x) for x in match.group('prog_list').split(',')]

        programs[prog_id] = prog_list

    # -Find the different groups-
    groups = []
    for prog in programs:
        group = find_group(prog, programs)

        if prog == 0:
            print('Num programs in group 0: ', len(group))

        # Compare each group (which is a set) and then add it to the list if new
        if group not in groups:
            groups.append(group)

    print('Number of groups: ', len(groups))


def find_group(program_num, program_dict):
    current_group = [program_num]

    for p_id in current_group:
        p_list = program_dict[p_id]

        for p in p_list:
            if p not in current_group:
                current_group.append(p)

    # By casting the list into a set it removes any duplicates and simplifies comparing one
    # group against another. setA == setB is very fast to compute, even though they are unordered
    return set(current_group)


def load_puzzle():
    f = open('day12input.txt', 'r')

    return [x.strip('\n') for x in f.readlines()]


if __name__ == '__main__':
    #in_data = [x for x in (TEST.strip('\n')).split('\n')]
    in_data = load_puzzle()

    digital_plumber(in_data)
