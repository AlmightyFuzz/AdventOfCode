import re
from itertools import product

TEST = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]


def parse_claim(claim_data):
    rgx = r'#(?P<cID>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<x_range>\d+)x(?P<y_range>\d+)'

    matches = re.search(rgx, claim_data)

    claim = Claim(matches.group('cID'))
    claim.set_area(
        int(matches.group('x')),
        int(matches.group('x_range')),
        int(matches.group('y')),
        int(matches.group('y_range'))
    )

    return claim


class Claim(object):
    def __init__(self, _ID):
        self.ID = _ID
        self.area = set()

    def set_area(self, x, x_range, y, y_range):
        x_vals = [x + i for i in range(x_range)]
        y_vals = [y + i for i in range(y_range)]

        self.area = set(product(x_vals, y_vals))


def find_overlapping_amount(claims):
    overlapping = set()

    for idx, this_claim in enumerate(claims):
        for that_claim in claims[idx + 1:]:
            # check if there is any overlap between the two areas
            if(not this_claim.area.isdisjoint(that_claim.area)):
                common = this_claim.area & that_claim.area
                # adds common set to overlapping set
                overlapping |= common

    print('Num common: ' + str(len(overlapping)))


def find_no_overlap(claims):
    overlapped_IDs = set()
    all_IDs = set([claim.ID for claim in claims])

    for idx, this_claim in enumerate(claims):
        for that_claim in claims[idx + 1:]:
            if(not this_claim.area.isdisjoint(that_claim.area)):
                overlapped_IDs.add(this_claim.ID)
                overlapped_IDs.add(that_claim.ID)

    print('ID with no overlap: ' + str(all_IDs - overlapped_IDs))


if __name__ == "__main__":
    # puzzle_data = TEST
    puzzle_data = [line.strip('\n')
                   for line in open('InputData/day3Input.txt', 'r')]

    claims = [parse_claim(claim_data) for claim_data in load_puzzle_data()]

    # find_overlapping_amount(claims)
    find_no_overlap(claims)
