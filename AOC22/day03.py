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

def split_input(puz_input):
    groups = []
    step = 3

    for i in range(0, len(puz_input), step):
        groups.append(puz_input[i:i+step])

    return groups

def find_badge_items(groups):
    badge_items = []

    for group in groups:
        first = set(group[0])
        second = set(group[1])
        third = set(group[2])

        badge = first & second & third
        badge_items.append(*badge)

    return badge_items

if __name__ == "__main__":
    #puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day03.txt")

    # common_items = find_common_items(puz_input)
    # priority_sum = compute_priority(common_items)

    groups = split_input(puz_input)
    badge_items = find_badge_items(groups)
    score = compute_priority(badge_items)

    print(score)