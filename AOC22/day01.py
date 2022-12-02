import common

TEST_DATA = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def find_largest_group(calories):
    totals = [sum(group) for group in calories]
    sort = sorted(totals, reverse=True)
    
    return sort[0]

def find_three_largest_group(calories):
    totals = [sum(group) for group in calories]
    sort = sorted(totals, reverse=True)

    return sum(sort[0:3:])

if __name__ == "__main__":
    # puz_input = TEST_DATA
    puz_input = open("data/day01.txt").read()
    calories = [[int(line) for line in group.split("\n")] for group in puz_input.split("\n\n")]

    # largest = find_largest_group(calories)
    largest = find_three_largest_group(calories)
    print(largest)