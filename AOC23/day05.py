import sys

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


def do_thing(seeds, almanac):
    lowest_location = sys.maxsize

    for seed in seeds:

        soil = apply_map(seed, almanac[1])
        fert = apply_map(soil, almanac[2])
        water = apply_map(fert, almanac[3])
        light = apply_map(water, almanac[4])
        temp = apply_map(light, almanac[5])
        humidity = apply_map(temp, almanac[6])
        location = apply_map(humidity, almanac[7])

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


def do_new_thing(seed_ranges, almanac):
    transformed_ranges = seed_ranges

    for page in almanac[1:]:
        changes = []

        for map in page:
            map_range = map[0]
            offset = map[1]

            for i, _range in enumerate(transformed_ranges):

                if _range.stop <= map_range.start or _range.start >= map_range.stop:
                    # fully outside
                    continue

                if _range.start >= map_range.start and _range.stop <= map_range.stop:
                    # fully inside
                    changes.append([i, offset])
                    continue

                if _range.start >= map_range.start and _range.start < map_range.stop:
                    # start falls inside map range
                    changed = range(_range.start, map_range.stop)
                    transformed_ranges[i] = changed
                    changes.append([i, offset])

                    new = range(map_range.stop, _range.stop)
                    transformed_ranges.append(new)
                    continue

                if _range.stop > map_range.start and _range.stop < map_range.stop:
                    # end falls inside map range
                    changed = range(map_range.start, _range.stop)
                    transformed_ranges[i] = changed
                    changes.append([i, offset])

                    new = range(_range.start, map_range.start)
                    transformed_ranges.append(new)
                    continue

                if _range.start < map_range.start and _range.stop > map_range.stop:
                    # spans across whole map
                    changed = range(map_range.start, map_range.stop)
                    transformed_ranges[i] = changed
                    changes.append([i, offset])

                    new_before = range(_range.start, map_range.start)
                    new_after = range(map_range.stop, _range.stop)
                    transformed_ranges.append(new_before)
                    transformed_ranges.append(new_after)

        for change in changes:
            (index, offset) = change
            r = transformed_ranges[index]
            transformed_ranges[index] = range(r.start + offset, r.stop + offset)

    lowest_location = min([r.start for r in transformed_ranges])
    print(f"lowest location: {lowest_location}")


if __name__ == "__main__":
    # puz_input = TEST_DATA
    puz_input = open("data/day05.txt").read()

    almanac = read_almanac(puz_input)
    seeds_nums = almanac[0]

    # Pt 1
    # do_thing(seeds_nums, almanac)

    # Pt 2
    pairs = [seeds_nums[s : s + 2] for s in range(0, len(seeds_nums), 2)]
    ranges = [range(p[0], p[0] + p[1]) for p in pairs]

    seeds = do_new_thing(ranges, almanac)
