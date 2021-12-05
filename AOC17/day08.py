import re

TEST = '''
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
'''

# The REGISTERS dict holds the register's name and its value
REGISTERS = dict()
LARGEST_VAL = 0


def process_instructions(instructions):

    data_regex = r'(?P<reg_name>[a-z]+) (?P<op>inc|dec) (?P<value>-?\d+) (?P<condition>.*)'

    for instruc in instructions:
        data_match = re.match(data_regex, instruc)

        reg = data_match.group('reg_name')
        op = data_match.group('op')
        change_value = int(data_match.group('value'))
        condition_str = data_match.group('condition')

        if condition(condition_str):
            set_register_value(reg, op, change_value)

    print('Final max:', max(REGISTERS.values()))
    print('Largest val:', LARGEST_VAL)


def condition(condition_str):
    condition_regex = r'if (?P<if_reg>[a-z]+) (?P<comp>.{1,2}) (?P<value>-?\d+)'
    cond_match = re.match(condition_regex, condition_str)

    if_reg = cond_match.group('if_reg')
    comparision = cond_match.group('comp')
    cond_value = int(cond_match.group('value'))

    if comparision == '>':
        return register_value(if_reg) > cond_value

    if comparision == '>=':
        return register_value(if_reg) >= cond_value

    if comparision == '<':
        return register_value(if_reg) < cond_value

    if comparision == '<=':
        return register_value(if_reg) <= cond_value

    if comparision == '==':
        return register_value(if_reg) == cond_value

    if comparision == '!=':
        return register_value(if_reg) != cond_value


def register_value(reg):
    if reg in REGISTERS:
        return REGISTERS[reg]
    else:
        REGISTERS[reg] = 0
        return 0


def set_register_value(reg, op, value):
    if reg not in REGISTERS:
        REGISTERS[reg] = 0

    global LARGEST_VAL
    if op == 'inc':
        REGISTERS[reg] = REGISTERS[reg] + value

        if REGISTERS[reg] > LARGEST_VAL:
            LARGEST_VAL = REGISTERS[reg]
    elif op == 'dec':
        REGISTERS[reg] = REGISTERS[reg] - value

        if REGISTERS[reg] > LARGEST_VAL:
            LARGEST_VAL = REGISTERS[reg]


def load_test():
    data = TEST.strip('\n')
    return data.split('\n')


def load_puzzle():
    f = open('day8input.txt')

    data = [line.strip('\n') for line in f]

    return data


if __name__ == '__main__':
    # INSTRUCTIONS = load_test()
    INSTRUCTIONS = load_puzzle()

    process_instructions(INSTRUCTIONS)
