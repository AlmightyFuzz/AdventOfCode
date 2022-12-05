import common

TEST_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

# index+1 of item equals priority
PRIORITY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def find_common_items(rucksacks):
    common_items = list()

    for sack in rucksacks:
        mid_point = int(len(sack) / 2)
        first_comp = set(sack[0 : mid_point])
        second_comp = set(sack[mid_point : len(sack)])

        common_item = first_comp & second_comp # set intersection
        common_items.append(*common_item) # * =>  unpack iterable

    return common_items

def compute_priority(common_items):
    total = 0

    for item in common_items:
        p = PRIORITY.index(item) + 1
        total += p

    return total

if __name__ == "__main__":
    #puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day03.txt")

    common_items = find_common_items(puz_input)
    priority_sum = compute_priority(common_items)

    print(priority_sum)