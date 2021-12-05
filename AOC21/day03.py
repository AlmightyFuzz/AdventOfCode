import common
from collections import Counter

TEST_DATA = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def find_most_common_bit(data, bit_index):
    bits = [number[bit_index] for number in data]
    count = Counter(bits)
    
    if count["0"] == count["1"]:
        return "1"
    else:
        return count.most_common(1)[0][0] # [("0", 5)]

def read_power_consumption(data):
    gamma = ""
    epsilon = ""
    length = len(data[0])

    for bit_index in range(length):
        most_common = find_most_common_bit(data, bit_index)

        if most_common == "0":
            gamma += "0"
            epsilon += "1"
        elif most_common == "1":
            gamma += "1"
            epsilon += "0"

    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    print(f"Gamma: {gamma} = {gamma_dec}")
    print(f"Epsilon: {epsilon} = {epsilon_dec}")
    print(f"Result: {gamma_dec * epsilon_dec}")

def find_oxygen_rating(data, bit_index = 0):
    most_common = find_most_common_bit(data, bit_index)
    remaining = [number for number in data if (number[bit_index] == most_common)]
    
    if len(remaining) <= 1:
        return remaining[0]
    else:
        return find_oxygen_rating(remaining, bit_index + 1)

def find_co2_rating(data, bit_index = 0):
    most_common = find_most_common_bit(data, bit_index)
    remaining = [number for number in data if (number[bit_index] != most_common)]

    if len(remaining) <= 1:
        return remaining[0]
    else:
        return find_co2_rating(remaining, bit_index + 1)

def find_life_support_rating(data):
    oxygen_rating = find_oxygen_rating(data)
    co2_rating = find_co2_rating(data)

    oxygen_dec = int(oxygen_rating, 2)
    co2_dec = int(co2_rating, 2)
    print(f"Oxygen rating: {oxygen_rating} = {oxygen_dec}")
    print(f"CO2 rating: {co2_rating} = {co2_dec}")
    print(F"Result: {oxygen_dec * co2_dec}")

if __name__ == "__main__":
    #data = common.load_test_data(TEST_DATA)
    data = common.load_puzzle_input("data/day03.txt")
    
    read_power_consumption(data)
    find_life_support_rating(data)