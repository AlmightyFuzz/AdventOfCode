TEST1 = "1212"
TEST2 = "1221"
TEST3 = "123425"
TEST4 = "123123"
TEST5 = "12131415"

PUZZLE_INPUT = ""

# Compare two consecutive digits to see if they match.
# Match the last digit to the first


def captcha(in_str):
    total = 0

    for pos, char in enumerate(in_str):

        # if at the end of the string look at the first
        if pos + 1 == len(in_str):
            if char == in_str[0]:
                total += int(char)
        else:
            if char == in_str[pos + 1]:
                total += int(char)

    return total

# Compare the digit with the one halfway along string.
# Wrap around to start of string when you've reached the end.


def captcha2(in_str):
    str_length = len(in_str)
    char_step = int(str_length / 2)
    total = 0

    for pos, char in enumerate(in_str):
        other_char_pos = pos + char_step

        # Loop around if you've the end of the string
        if other_char_pos >= str_length:
            if char == in_str[other_char_pos - str_length]:
                total += int(char)
        else:
            if char == in_str[other_char_pos]:
                total += int(char)

    return total


if __name__ == '__main__':
    # print(captcha2(TEST1))
    # print(captcha2(TEST2)) #0
    # print(captcha2(TEST3))
    # print(captcha2(TEST4)) #12
    # print(captcha2(TEST5))

    # print(captcha(PUZZLE_INPUT))
    print(captcha2(PUZZLE_INPUT))
