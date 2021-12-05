test_data = """1721
979
366
299
675
1456"""


def find_two_2020(values):

    for i in range(0, len(values)):
        first = values[i]
        rest = values[i+1:]

        for j in range(0, len(rest)):
            second = rest[j]

            if(first + second == 2020):
                return (first, second)


def find_three_2020(values):

    for i in range(0, len(values)):
        first = values[i]
        rest = values[i+1:]

        for j in range(0, len(rest)):
            second = rest[j]
            remaining = rest[j+1:]

            for k in range(0, len(remaining)):
                third = remaining[k]

                if(first + second + third == 2020):
                    return (first, second, third)


def get_puzzle_input():
    with open('InputData/day1.txt', 'r') as file:
        file_data = [line.strip('\n') for line in file]

        return [int(x) for x in file_data]


if __name__ == "__main__":
    #data = [int(x) for x in test_data.split('\n')]
    data = get_puzzle_input()

    nums = find_two_2020(data)
    print(nums[0] * nums[1])

    nums = find_three_2020(data)
    print(nums[0] * nums[1] * nums[2])
