import common

TEST_DATA_1 = """38006F45291200"""
TEST_DATA_2 = """EE00D40C823060"""
TEST_DATA_3 = """8A004A801A8002F478"""
TEST_DATA_4 = """620080001611562C8802118E34"""
TEST_DATA_5 = """C0015000016115A2E0802F182340"""
TEST_DATA_6 = """A0016C880162017C3686B18A3D4780"""


def parse_data(data):
    # input here are single lines, but common loading functions
    # expect inputs with multiple lines
    return data[0]


if __name__ == "__main__":
    data = common.load_test_data(TEST_DATA_1)
    # data = common.load_test_data(TEST_DATA_2)
    # data = common.load_test_data(TEST_DATA_3)
    # data = common.load_test_data(TEST_DATA_4)
    # data = common.load_test_data(TEST_DATA_5)
    # data = common.load_test_data(TEST_DATA_6)

    # data = common.load_test_data("data/day16.txt")

    hex_string = parse_data(data)

    print()
