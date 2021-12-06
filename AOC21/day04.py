import common

TEST_DATA = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def process_data(data):
    bingo_values = [int(x) for x in data[0].split(',')]

    data = data[2:]
    bingo_cards = []

    i = 0
    while i < len(data):
        card_data = data[i:i+5]
        # each card has two entries, [number, is_marked]
        card = [[[int(x), 0] for x in line.split(' ') if x != '']
                for line in card_data]
        bingo_cards.append(card)

        i += 6

    return (bingo_values, bingo_cards)


def mark_card(bingo_card, value):
    width = len(bingo_card[0])
    height = len(bingo_card)

    for x in range(width):
        for y in range(height):
            if bingo_card[x][y][0] == value:
                bingo_card[x][y][1] = 1

                return


def check_cards_for_bingo(score_cards):
    for card_idx, card in enumerate(score_cards):

        for row in card:
            marks = [space[1] for space in row]
            if sum(marks) == 5:
                # bingo!
                return card_idx

        columns = [[row[i] for row in card] for i in range(5)]

        for col in columns:
            marks = [space[1] for space in col]
            if sum(marks) == 5:
                # bingo!
                return card_idx

    return None


def run_the_numbers(bingo_data):
    bingo_numbers, bingo_cards = bingo_data

    for num in bingo_numbers:
        for card in bingo_cards:
            mark_card(card, num)

        card_num = check_cards_for_bingo(bingo_cards)

        if card_num != None:
            print("Bingo!")

            winning_card = bingo_cards[card_num]

            sum_unmarked = 0
            for x in range(len(winning_card[0])):
                for y in range(len(winning_card)):
                    if winning_card[x][y][1] == 0:
                        sum_unmarked += winning_card[x][y][0]

            print(f"Number: {num}")
            print(f"Winning card: {card_num}")
            print(f"Sum: {sum_unmarked}")
            print(f"Result: {num * sum_unmarked}")

            break


if __name__ == "__main__":
    #data = common.load_test_data(TEST_DATA)
    data = common.load_puzzle_input("data/day04.txt")

    bingo_data = process_data(data)
    run_the_numbers(bingo_data)
