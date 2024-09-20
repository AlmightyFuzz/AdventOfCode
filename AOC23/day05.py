import re
import sys
import common

TEST_DATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def read_almanac(puz_input):
    maps = puz_input.split("\n\n")

    seed_str = maps[0].split(": ")[1]
    seeds = [int(s) for s in seed_str.split(" ")]

    soil_str = extract_string(section=1, data=maps)
    soil_nums = extract_data(soil_str)
    soil = calculate_map_conversions(soil_nums)

    fertilizer_str = extract_string(section=2, data=maps)
    fertilizer_nums = extract_data(fertilizer_str)
    fertilizer = calculate_map_conversions(fertilizer_nums)

    water_str = extract_string(section=3, data=maps)
    water_nums = extract_data(water_str)
    water = calculate_map_conversions(water_nums)

    light_str = extract_string(section=4, data=maps)
    light_nums = extract_data(light_str)
    light = calculate_map_conversions(light_nums)

    temp_str = extract_string(section=5, data=maps)
    temp_nums = extract_data(temp_str)
    temp = calculate_map_conversions(temp_nums)

    humidity_str = extract_string(section=6, data=maps)
    humidity_nums = extract_data(humidity_str)
    humidity = calculate_map_conversions(humidity_nums)

    location_str = extract_string(section=7, data=maps)
    location_nums = extract_data(location_str)
    location = calculate_map_conversions(location_nums)

    return [seeds, soil, fertilizer, water, light, temp, humidity, location]


def extract_string(section, data):
    s = data[section].split(":\n")[1]
    return s.strip("\n")


def extract_data(data_str):
    return [[int(x) for x in l.split(" ")] for l in data_str.split("\n")]


def calculate_map_conversions(map):
    """Returns a tuple containing the set of source values and a conversion to convert from source to destination"""
    return [(range(m[1], m[1] + m[2]), m[0] - m[1]) for m in map]


def do_thing(almanac):
    lowest_location = sys.maxsize

    seeds = almanac[0]

    for seed in seeds:
        print(f"seed: {seed}")

        soil = apply_map(seed, almanac[1])
        print(f"soil: {soil}")

        fert = apply_map(soil, almanac[2])
        print(f"fertilizer: {fert}")

        water = apply_map(fert, almanac[3])
        print(f"water: {water}")

        light = apply_map(water, almanac[4])
        print(f"light: {light}")

        temp = apply_map(light, almanac[5])
        print(f"temperature: {temp}")

        humidity = apply_map(temp, almanac[6])
        print(f"humidity: {humidity}")

        location = apply_map(humidity, almanac[7])
        print(f"location: {location}\n")

        if location < lowest_location:
            lowest_location = location

    print(f"lowest_location: {lowest_location}")


def apply_map(current_val, mapping):
    current = current_val

    for map in mapping:
        if current in map[0]:
            current += map[1]
            break

    return current


if __name__ == "__main__":
    # puz_input = TEST_DATA
    puz_input = open("data/day05.txt").read()

    almanac = read_almanac(puz_input)
    do_thing(almanac)
