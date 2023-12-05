import common
import re

TEST_DATA = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

def find_calibration_values(input):
    total = 0

    for line in input:
        digits = ""

        for c in line:
            if re.match(r"\d", c):
                digits += c
                break

        for c in line[::-1]:
            if re.match(r"\d", c):
                digits += c
                break
        
        print(digits)
        total += int(digits)

    return total


if __name__ == "__main__":
    #puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day01.txt")

    result = find_calibration_values(puz_input)

    print(result)