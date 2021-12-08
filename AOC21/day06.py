import common

TEST_DATA = """3,4,3,1,2"""

def parse_input(data):
    fish = [int(f) for f in data.split(',')]
    return fish

# Keep track of each fish individually. Fine for small values but quickly
# produces vast number of entities and becomes too slow to process for larger values
def simulate_fish_naive(fish, num_days):
    for _ in range(num_days):
        new_fish = []

        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                new_fish.append(8)
            else:
                fish[i] -= 1

        fish += new_fish

    print(F"Num fish: {len(fish)}")

# Keep track of the total number of fish at certain ages. This keeps the data set quite small
# with only the individual values becoming very large.
# This is a Entity Component System (ECS) approach to the problem.
def simulate_fish(initial_fish, num_days):
    ages = {x: 0 for x in range(9)}

    for fish in initial_fish:
        ages[fish] += 1

    for _ in range(num_days):
        new_fish = 0
        for age in range(9):
            if age == 0:
                new_fish = ages[0]
            else:
                num = ages[age]
                ages[age - 1] = num

        ages[6] += new_fish
        ages[8] = new_fish

    num_fish = sum(ages.values())
    print(f"Num fish: {num_fish}")

if __name__ == "__main__":
    #data = common.load_test_data(TEST_DATA)
    data = common.load_puzzle_input("data/day06.txt")

    fish = parse_input(data[0])

    #simulate_fish_naive(fish, num_days=80)
    simulate_fish(fish, num_days=256)
