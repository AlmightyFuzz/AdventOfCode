import re

TEST = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""


def parse_input(input_data):
    regex = r'Step ([A-Z]).*step ([A-Z])'
    steps = []

    for data in input_data:
        match = re.search(regex, data)
        before = match.group(1)
        after = match.group(2)

        steps.append((before, after))

    return steps


def find_first_last_step(step_dependencies):
    befores = set([dependency[0] for dependency in step_dependencies])
    afters = set([dependency[1] for dependency in step_dependencies])

    first = befores - afters
    last = afters - befores

    return tuple(first | last)


def find_next_steps(current_step, step_dependencies):
    return [(dep[1]) for dep in step_dependencies if dep[0] == current_step]


def process_steps(step_requirements):
    first_last = find_first_last_step(step_requirements)
    step_order = [first_last[0]]

    current_step = first_last[0]
    while(True):
        next_steps = find_next_steps(current_step, step_requirements)
        next_steps.sort()

        # How the hell???

    print(''.join(step_order))


if __name__ == "__main__":
    puzzle_data = TEST.split('\n')
    # puzzle_data = [line.strip('\n')
    #               for line in open('InputData/day7input.txt', 'r')]

    step_requirements = parse_input(puzzle_data)
    process_steps(step_requirements)
