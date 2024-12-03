import common

TEST_DATA = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def count_safe(reports):
    safe_count = 0

    for report in reports:
        is_increasing = False
        is_safe = True
        previous = report[0]

        for i, level in enumerate(report):
            if i == 0:
                continue

            if i == 1:
                is_increasing = level > previous

            diff = abs(level - previous)

            if diff < 1 or diff > 3:
                is_safe = False
                break

            if (is_increasing and level < previous) or (
                not is_increasing and level > previous
            ):
                is_safe = False
                break

            previous = level

        if is_safe:
            safe_count += 1

    print("Safe count: " + str(safe_count))


if __name__ == "__main__":
    # puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day02.txt")

    reports = [[int(level) for level in report.split(" ")] for report in puz_input]

    count_safe(reports)
