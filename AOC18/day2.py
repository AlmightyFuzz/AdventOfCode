from collections import Counter

TEST1 = 'abcdef'  # 0     # 0
TEST2 = 'bababc'  # 2a 3b # 2, 3
TEST3 = 'abbcde'  # 2b    # 2
TEST4 = 'abcccd'  # 3c    # 3
TEST5 = 'aabcdd'  # 2a 2d # 2
TEST6 = 'abcdee'  # 2e    # 2
TEST7 = 'ababab'  # 3a 3b # 3

TEST_INPUT = [TEST1, TEST2, TEST3, TEST4, TEST5, TEST6, TEST7]

ID_TEST = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']


def find_pairs_triplets(input):
    item_counter = Counter(input)
    unique_items = set(input)
    vals = set()

    if(len(input) == len(unique_items)):
        # No repetitions
        return vals

    for item in unique_items:
        if item_counter[item] == 2:
            vals.add(2)
        if item_counter[item] == 3:
            vals.add(3)

    # contains '2' if a pair is present
    # contains '3' if a triplet is present
    return list(vals)


def find_checksum(input):
    pairs_triplets = [find_pairs_triplets(item) for item in input]

    # take each item in the inner list in the list of lists pairs_triplets
    ls = [item for inner_list in pairs_triplets for item in inner_list]

    group_counter = Counter(ls)
    checksum = (group_counter[2] * group_counter[3])
    print("Checksum: " + str(checksum))


def find_similar_ID(input):
    the_IDs = ()

    for idx, this_ID in enumerate(input):
        for that_ID in input[idx + 1:]:
            if (similiar_IDs(this_ID, that_ID)):
                the_IDs = (this_ID, that_ID)
                break

    compare_IDs(the_IDs)


def compare_IDs(IDs):
    common_chars = []

    zipped = zip(IDs[0], IDs[1])
    for pair in zipped:
        if(pair[0] == pair[1]):
            common_chars.append(pair[0])

    print("Common: " + ''.join(common_chars))


def similiar_IDs(this_ID, that_ID):
    unequal_count = 0
    zipped_IDs = zip(this_ID, that_ID)

    for pair in zipped_IDs:
        if(pair[0] != pair[1]):
            unequal_count += 1

            if(unequal_count >= 2):
                break

    return unequal_count == 1


if __name__ == "__main__":
    # puzzle_input = TEST_INPUT
    puzzle_input = [line.strip('\n')
                    for line in open('InputData/day2Input.txt', 'r')]

    # find_checksum(puzzle_input)
    find_similar_ID(puzzle_input)
