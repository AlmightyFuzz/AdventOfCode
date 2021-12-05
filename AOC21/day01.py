import common


TEST_DATA = """199
200
208
210
200
207
240
269
260
263"""

def count_depth_increases(data):
    count = 0
    length = len(data)

    for i in range(length):
        if i >= length - 1:
            break

        if data[i+1] > data[i]:
            count += 1

    return count

def create_window_sums(data):
    length = len(data)
    window_sums = []

    for i in range(length):
        if i >= length - 2:
            break

        window = data[i:i+3]
        window_sums.append(sum(window))

    return window_sums


if __name__ == "__main__":
    #raw = common.process_test_data(TEST_DATA)
    raw = common.load_puzzle_input("data/day01.txt")
    data = [int(x) for x in raw]
    
    window_values = create_window_sums(data)
    count = count_depth_increases(window_values)

    print("Count: ", count)