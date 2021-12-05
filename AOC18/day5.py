from string import ascii_lowercase, ascii_uppercase

TEST = 'dabAcCaCBAcCcaDA'
LOWER_TO_UPPER = {ch: ascii_uppercase[i]
                  for i, ch in enumerate(ascii_lowercase)}
UPPER_TO_LOWER = {ch: ascii_lowercase[i]
                  for i, ch in enumerate(ascii_uppercase)}
PAIRS = {**LOWER_TO_UPPER, **UPPER_TO_LOWER}  # merge dictinaries into one


def react_polymer(polymer):
    final_polymer = ['.']  # '.' is filler char needed for algorithm

    for c in polymer:
        d = final_polymer[-1]

        # if current char pairs with last char in final polymer
        if d in PAIRS.keys() and c == PAIRS[d]:
            final_polymer.pop()
        else:
            final_polymer.append(c)

        # step over to next char in polymer

    return ''.join(final_polymer[1:])


def find_shortest_polymer(polymer):
    shortest = len(polymer)

    for l_item, u_item in PAIRS.items():
        modified_polymer = polymer.replace(u_item, l_item)
        modified_polymer = modified_polymer.replace(l_item, '')

        length = len(react_polymer(modified_polymer))
        if length < shortest:
            shortest = length

    print('Shortest: ' + str(shortest))


if __name__ == "__main__":
    # polymer = TEST
    polymer = [line.strip('\n')
               for line in open('InputData/day5Input.txt', 'r')][0]

    find_shortest_polymer(polymer)
