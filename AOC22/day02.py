import common

TEST_DATA = """A Y
B X
C Z"""

def win_or_lose(round):
    them = round[0]
    me = round[2]

    if them == 'A': # rock
        if me == 'X': return 3 # rock
        if me == 'Y': return 6 # paper
        if me == 'Z': return 0 # scissors

    if them == 'B': # paper
        if me == 'X': return 0 # rock
        if me == 'Y': return 3 # paper
        if me == 'Z': return 6 # scissors

    if them == 'C': # scissors
        if me == 'X': return 6 # rock
        if me == 'Y': return 0 # paper
        if me == 'Z': return 3 # scissors

def calculate_score(puz_input):
    score = 0

    for round in puz_input:
        round_score = win_or_lose(round)

        if round[2] == 'X': round_score += 1
        if round[2] == 'Y': round_score += 2
        if round[2] == 'Z': round_score += 3

        score += round_score

    return score

if __name__ == "__main__":
    # puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day02.txt")

    score = calculate_score(puz_input)

    print(score)