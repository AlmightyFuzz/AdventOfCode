import common
from statistics import median

TEST_DATA = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def parse_for_syntax_error(line):
    opening = set(['(', '[', '{', '<'])
    closing = set([')', ']', '}', '>'])

    stack = []

    for c in line:
        if c in opening:
            stack.append(c)

        if c in closing:
            b = stack.pop()

            if (c == ')' and b != '('
                or c == ']' and b != '['
                or c == '}' and b != '{'
                    or c == '>' and b != '<'):

                return c

    return stack


def score_syntax_errors(data):
    score = 0

    for line in data:
        error = parse_for_syntax_error(line)

        if error == ')':
            score += 3
        elif error == ']':
            score += 57
        elif error == '}':
            score += 1197
        elif error == '>':
            score += 25137

    print(f"Score: {score}")


def calculate_autocomplete_score(incomplete_chars):
    score = 0

    for c in incomplete_chars:
        score = score * 5

        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4

    return score


def score_incomplete_lines(data):
    scores = []

    for line in data:
        result = parse_for_syntax_error(line)

        if isinstance(result, list):
            incomplete_chars = result[::-1]  # reverse

            score = calculate_autocomplete_score(incomplete_chars)
            scores.append(score)

    print(f"Middle score: {median(scores)}")


if __name__ == "__main__":
    #data = common.load_test_data(TEST_DATA)
    data = common.load_puzzle_input("data/day10.txt")

    # score_syntax_errors(data) # pt1
    score_incomplete_lines(data)
