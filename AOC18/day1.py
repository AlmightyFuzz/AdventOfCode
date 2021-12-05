TEST1 = '+1, +1, +1'
TEST2 = '+1, +1, -2'
TEST3 = '-1, -2, -3'

DUP_TEST1 = '+1, -1'  # result = 0
DUP_TEST2 = '+3, +3, +4, -2, -4'  # result = 10
DUP_TEST3 = '-6, +3, +8, +5, -6'  # result = 5
DUP_TEST4 = '+7, +7, -2, -7, -4'  # result = 14


def find_total(input):
    total = 0

    for item in input:
        total += int(item)

    return total


def find_repeated_value(input):
    running_total = 0
    # searching a set is O(1), while searching a list is O(n)
    previous_values = set()
    previous_values.add(0)
    duplicate = 0

    index = 0
    loop_num = 0
    while(True):
        running_total += int(input[index])

        if(running_total in previous_values):
            duplicate = running_total
            break

        previous_values.add(running_total)

        index += 1
        if(index > len(input) - 1):
            index = 0

        loop_num += 1

    print(loop_num)
    print("Size of set: " + str(len(previous_values)))
    return duplicate


def test_solution(test_input):
    # total = find_total(test_input.split(','))
    duplicate = find_repeated_value(test_input.split(','))

    print("Duplicate: " + str(duplicate))


def process_puzzle_input():
    with open('InputData/day1Input.txt', 'r') as file:
        file_data = [line.strip('\n') for line in file]

    # total = find_total(file_data)
    duplicate = find_repeated_value(file_data)

    print('Puzzle Duplicate: ' + str(duplicate))


if __name__ == "__main__":
    # test_solution(TEST1)
    # test_solution(TEST2)
    # test_solution(TEST3)
    # process_puzzle_input()

    # test_solution(DUP_TEST1)
    # test_solution(DUP_TEST2)
    # test_solution(DUP_TEST3)
    # test_solution(DUP_TEST4)

    process_puzzle_input()
