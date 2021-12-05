import re
from collections import namedtuple

test_data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


def validate_passwords1(database):
    valid = 0

    for record in database:
        record = parse_input(record)

        letter_count = record.password.count(record.Policy.letter)
        min_num = record.Policy.a
        max_num = record.Policy.b

        if min_num <= letter_count and letter_count <= max_num:
            valid += 1

    return valid


def validate_passwords2(database):
    valid = 0

    for record in database:
        record = parse_input(record)

        char1 = record.password[record.Policy.a - 1]
        char2 = record.password[record.Policy.b - 1]

        if (char1 == record.Policy.letter) ^ (char2 == record.Policy.letter):  # ^ == XOR
            valid += 1

    return valid


def parse_input(string):
    match = re.match(r"(\d+)-(\d+) (\D): (\D+)", string)
    min_num = int(match.group(1))
    max_num = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    Policy = namedtuple('Policy', 'a b letter')
    Record = namedtuple('Record', 'Policy password')

    return Record(Policy(min_num, max_num, letter), password)


def get_puzzle_input():
    with open('InputData/day2.txt', 'r') as file:
        file_data = [line.strip('\n') for line in file]

        return file_data


if __name__ == "__main__":
    #data = test_data.split('\n')
    data = get_puzzle_input()

    #num_valid = validate_passwords1(data)
    num_valid = validate_passwords2(data)

    print(num_valid)
