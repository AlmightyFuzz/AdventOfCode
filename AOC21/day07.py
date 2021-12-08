import common
from statistics import median

TEST_DATA = """16,1,2,0,4,2,7,1,2,14"""

CACHED_FUEL_CALCULATION = dict()

def process_data(data):
    crabs = [int(pos) for pos in data.split(',')]
    return crabs

def find_efficient_position_simple(positions):
    optimal_pos = median(positions)

    spent_fuel = 0
    for pos in positions:
        spent_fuel += abs(pos - optimal_pos)

    print(f"Spent fuel: {spent_fuel}")

def find_efficient_position(positions):
    min_pos = min(positions)
    max_pos = max(positions)

    fuel_costs = {p: 0 for p in range(min_pos, max_pos+1)}

    for test_pos in fuel_costs.keys():
        fuel_spent = 0

        for pos in positions:
            distance = abs(pos - test_pos)
            fuel_spent += calculate_fuel_cost(distance)

        fuel_costs[test_pos] = fuel_spent

    print(f"Least fuel: {min(fuel_costs.values())}")

def calculate_fuel_cost(distance):
    if distance in CACHED_FUEL_CALCULATION:
        # don't repeat previous calculations
        return CACHED_FUEL_CALCULATION[distance]
    else:
        #fuel = sum([d for d in range(distance+1)])
        # cost of fuel for further distances is just Triangle Numbers,
        # which can be calculated as t = (n * (n+1)) / 2
        fuel = (distance * (distance + 1)) / 2
        CACHED_FUEL_CALCULATION[distance] = int(fuel)
        return fuel

if __name__ == "__main__":
    #data = common.load_test_data(TEST_DATA)
    data = common.load_puzzle_input("data/day07.txt")

    positions = process_data(data[0])

    #find_efficient_position_simple(positions) pt1
    find_efficient_position(positions)
