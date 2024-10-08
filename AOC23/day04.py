import common

TEST_DATA = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def find_total_points(cards):
    total_points = 0

    for card in cards:
        total_points += calculate_points(card)

    print(total_points)


def calculate_points(card):
    num_matches = find_number_of_matches(card)

    if num_matches == 0:
        return 0

    points = 2 ** (num_matches - 1)
    return points


def find_number_of_matches(card):
    card = card.replace("  ", " ")  # replace double spaces with one space

    just_numbers = card.split(": ")[1]
    numbers = just_numbers.split(" | ")
    winning_nums = [int(x) for x in numbers[0].split(" ")]
    my_nums = [int(x) for x in numbers[1].split(" ")]

    winning_nums = set(winning_nums)
    my_nums = set(my_nums)

    matches = winning_nums.intersection(my_nums)
    num_matches = len(matches)

    return num_matches


def find_total_scratchcards(card_data):
    cards = [[card, 1] for card in card_data]

    for i, card in enumerate(cards):

        for _ in range(card[1]):
            num_matches = find_number_of_matches(card[0])

            for x in range(i + 1, i + num_matches + 1):
                cards[x][1] += 1

    # algorithm is slow due to many loops, works but needs improving
    total_cards = sum([c[1] for c in cards])
    print(f"Total cards: {total_cards}")


if __name__ == "__main__":
    # puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day04.txt")

    # find_total_points(puz_input)
    find_total_scratchcards(puz_input)
