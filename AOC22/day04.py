import common

TEST_DATA = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def count_full_overlaps(pairs):
    num = 0

    for pair in pairs:
        first = pair[0]
        second = pair[1]

        if ((first[0] >= second[0] and first[1] <= second[1]) or
            (second[0] >= first[0] and second[1] <= first[1])):
            num += 1

    return num

def count_overlaps(pairs):
    num = 0

    for pair in pairs:
        first = pair[0]
        second = pair[1]

        if ((first[0] <= second[0] and first[1] >= second[0])
         or (first[0] <= second[1] and first[1] >= second[1])
         or (second[0] <= first[0] and second[1] >= first[0])
         or (second[0] <= first[1] and second[1] >= first[1])):
            num += 1

    return num

if __name__ == "__main__":
    #puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day04.txt")

    # split input by ',' then '-'
    ids = [[[int(z) for z in y.split('-')] for y in x.split(',')] for x in puz_input]
    
    full = count_full_overlaps(ids)
    partial = count_overlaps(ids)

    print(partial)