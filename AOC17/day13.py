import re

TEST = '''0: 3
1: 2
4: 4
6: 4'''


def infiltrate(scanner_data):
    # Populate dictionary
    scanners = dict()
    for data in scanner_data:
        match = re.match(r'(?P<depth>\d+): (?P<range>\d+)', data)

        s_depth = int(match.group('depth'))
        s_range = int(match.group('range'))
        scanners[s_depth] = s_range

    # Solve problem
    delay = 0
    sev = 0
    got_caught = False
    while True:
        for s_depth, s_range in scanners.items():
            # This is the period of oscillation, ie length of time it takes
            # for the scanner to travel to the end of its range and back to the start
            period = (s_range * 2 - 2)

            # If the modulo is 0 then the scanner is in position 0 when we entered that layer and we got caught
            if (delay + s_depth) % period == 0:
                if delay == 0:
                    sev += s_depth * s_range

                got_caught = True

        if delay == 0:
            print('Severity of leaving immediately: ', sev)

        # We found a delay that allows us to pass without getting caught
        if not got_caught:
            break

        got_caught = False
        delay += 1

    print('Wait for {0} picoseconds to get through'.format(delay))


def load_puzzle():
    f = open('day13input.txt')

    return [x.strip('\n') for x in f.readlines()]


if __name__ == '__main__':
    # in_data = [x.strip('\n') for x in TEST.split('\n')]
    in_data = load_puzzle()

    infiltrate(in_data)
