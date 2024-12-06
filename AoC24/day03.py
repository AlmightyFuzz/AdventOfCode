import common
import re

TEST_DATA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST_DATA2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def find_mul_instructions(memory_string):
    mul_rgx = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)")

    total = 0

    # returns a list of tuples, each tuple contains the values from each capture group in the pattern
    matches = mul_rgx.finditer(memory_string)

    is_do = True
    for match in matches:
        value = match.group(0)

        if value == "do()":
            is_do = True
        elif value == "don't()":
            is_do = False
        else:  # mul(x,y)
            if is_do:
                total += int(match.group(1)) * int(match.group(2))

    print("Total: " + str(total))


if __name__ == "__main__":
    # puz_input = TEST_DATA2
    puz_input = open("data/day03.txt", "r").read()

    find_mul_instructions(puz_input)
