import common

TEST_DATA = """3   4
4   3
2   5
1   3
3   9
3   3"""


def parse_numbers(numbers):
    left_list = []
    right_list = []

    for line in numbers:
        n = line.split("   ")
        left_list.append(int(n[0]))
        right_list.append(int(n[1]))

    return (left_list, right_list)


def pair_numbers(left_list, right_light):
    total_diff = 0

    left_list = sorted(left_list)
    right_light = sorted(right_light)

    for i in range(0, len(left_list)):
        total_diff += abs(left_list[i] - right_light[i])

    print("Total diff: " + str(total_diff))


def find_similarity(left_list, right_list):
    similarity = 0

    for num in left_list:
        count = right_list.count(num)

        similarity += num * count

    print("Similarity score: " + str(similarity))


if __name__ == "__main__":
    # puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day01.txt")

    ls = parse_numbers(puz_input)

    # pair_numbers(ls[0], ls[1])  # pt 1
    find_similarity(ls[0], ls[1])
