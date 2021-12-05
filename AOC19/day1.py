import math


def calculate_fuel_needed_for(mass):
    return math.floor(mass / 3) - 2


def calculate_extra_fuel(fuel):
    extra_fuel = calculate_fuel_needed_for(fuel)

    if extra_fuel > 0:
        extra_fuel += calculate_extra_fuel(extra_fuel)
    else:
        extra_fuel = 0

    return extra_fuel


def total_fuel(mass):
    component_fuel = calculate_fuel_needed_for(mass)
    extra_fuel = calculate_extra_fuel(component_fuel)

    return component_fuel + extra_fuel


def get_puzzle_input():
    with open('InputData/day1Input.txt', 'r') as file:
        file_data = [line.strip('\n') for line in file]
        return file_data


if __name__ == "__main__":
    # print(calculate_fuel(12))
    # print(calculate_fuel(14))
    # print(calculate_fuel(1969))
    # print(calculate_fuel(100756))

    component_masses = [int(s) for s in get_puzzle_input()]
    #component_masses = [100756]

    fuel_reqs = map(total_fuel, component_masses)
    components_fuel_req = sum(fuel_reqs)

    print(components_fuel_req)
