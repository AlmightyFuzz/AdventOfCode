import common

TEST_DATA = """A Y
B X
C Z"""

def win_or_lose(them, me):
    # them = round[0]
    # me = round[2]

    if them == 'A': # rock
        if me == 'A': return 3 # rock
        if me == 'B': return 6 # paper
        if me == 'C': return 0 # scissors

    if them == 'B': # paper
        if me == 'A': return 0 # rock
        if me == 'B': return 3 # paper
        if me == 'C': return 6 # scissors

    if them == 'C': # scissors
        if me == 'A': return 6 # rock
        if me == 'B': return 0 # paper
        if me == 'C': return 3 # scissors


def calculate_score(match_ups):
    score = 0

    for round in match_ups:
        them = round[0]
        me = round[1]
        round_score = win_or_lose(them, me)

        if me == 'A': round_score += 1
        if me == 'B': round_score += 2
        if me == 'C': round_score += 3

        score += round_score

    return score


def create_match_ups(round):
    them = round[0]
    expected = round[2]
    me = ''

    if expected == 'X': # lose
        if   them == 'A': me = 'C'
        elif them == 'B': me = 'A'
        elif them == 'C': me = 'B'

    elif expected == 'Y': # draw
        if   them == 'A': me = 'A'
        elif them == 'B': me = 'B'
        elif them == 'C': me = 'C'

    elif expected == 'Z': # win
        if   them == 'A': me = 'B'
        elif them == 'B': me = 'C'
        elif them == 'C': me = 'A'

    return (them, me)

def create_strategy(puz_input):
    match_ups = [create_match_ups(x) for x in puz_input]

    return calculate_score(match_ups)

if __name__ == "__main__":
    #puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day02.txt")

    score = create_strategy(puz_input)

    print(score)