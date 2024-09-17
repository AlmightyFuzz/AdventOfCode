import common
import re

TEST_DATA = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST_DATA2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def find_calibration_values(input):
    total = 0
    rx = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)")

    for line in input:
        digits = ""

        match = rx.search(line)
        digits += word_to_digit(match[0])

        for i in range(len(line)):
            i += 1
            s = line[-i::]
            match = rx.match(s)
            if match:
                digits += word_to_digit(match[0])
                break

        print(digits)
        total += int(digits)

    return total


def word_to_digit(word):
    if word == "one":
        return "1"
    elif word == "two":
        return "2"
    elif word == "three":
        return "3"
    elif word == "four":
        return "4"
    elif word == "five":
        return "5"
    elif word == "six":
        return "6"
    elif word == "seven":
        return "7"
    elif word == "eight":
        return "8"
    elif word == "nine":
        return "9"

    return word


if __name__ == "__main__":
    # puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_test_data(TEST_DATA2)
    # puz_input = common.load_puzzle_input("data/day01.txt")

    result = find_calibration_values(puz_input)

    print(result)
