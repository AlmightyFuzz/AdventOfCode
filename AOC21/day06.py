import common


TEST_DATA = """3,4,3,1,2"""


def parse_input(data):
    fish = [int(f) for f in TEST_DATA.split(',')]
    return fish

def simulate_fish(fish, num_days):
    return fish

if __name__ == "__main__":
    data = common.load_test_data(TEST_DATA)
    # data = common.load_puzzle_input("data/day06.txt")

    fish = parse_input(data)

    print(fish)
