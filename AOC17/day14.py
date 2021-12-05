from day10 import knot_hash2

TEST = 'flqrgnkx'
PUZZLE_INPUT = 'ugkiagan'


def compute_hashes_and_save():
    '''Computes the hash data and saves the resulting hash strings'''

    disk_data = [TEST + '-' + str(i) for i in range(128)]
    with open('day14data\\TEST.txt', 'w') as f:
        for row in disk_data:
            f.write(knot_hash2(row) + '\n')

    disk_data = [PUZZLE_INPUT + '-' + str(i) for i in range(128)]
    with open('day14data\\PUZZLE_INPUT.txt', 'w') as f:
        for row in disk_data:
            f.write(knot_hash2(row) + '\n')


def populate_disk(hash_list):
    '''Converts the hex values in the hashes to binary and then populates the disk with that data'''

    disk = [[0 for x in range(128)] for y in range(128)]
    count = 0

    for x, hash_str in enumerate(hash_list):
        binary_str = ''

        for hex_digit in hash_str:
            # int(hex, 16) converts the hex value to an int, which bin() then converts to binary
            binary = bin(int(hex_digit, 16))

            # python prefixes binary with '0b' and doesn't include leading zeros,
            # so we slice off the prefix and pad the string
            binary = binary[2:].zfill(4)

            # Concat the binary results into one long string
            binary_str += binary

        for y, ch in enumerate(binary_str):
            if ch == '1':
                count += 1

            disk[x][y] = int(ch)

    print('Used squares: ', count)

    return disk


def find_regions(disk_data):
    '''Finds the number of unique regions'''

    # (x,y) = region_id
    regions = dict()
    region_id = 0

    for row_num, row_data in enumerate(disk_data):
        for column_num, column_data in enumerate(row_data):
            if column_data == 0:
                continue
            else:
                if (row_num, column_num) not in regions:
                    flood_fill((row_num, column_num), disk_data,
                               regions, region_id)

                    region_id += 1

    # Creates a Set out the region values to remove duplicates
    print('Num regions: ', len(set(regions.values())))


def flood_fill(coord, disk, region_dict, region_id):
    '''
    Uses the flood fill algorithm to find the region of used disk space
    connected to given coordinate, and then updates the region dict with that information
    '''

    try:
        # Negative indexes are valid in python and don't produce an indexOutOfRange exception
        if coord[0] < 0 or coord[1] < 0:
            return
        if disk[coord[0]][coord[1]] == 0:
            return
    except IndexError:
        # Catches coord values that are too big
        return

    if coord in region_dict:
        return

    # Coord is a new, valid region
    region_dict[coord] = region_id

    # Check if the surrounding coords are also part of the region
    flood_fill((coord[0] + 1, coord[1]), disk, region_dict, region_id)
    flood_fill((coord[0] - 1, coord[1]), disk, region_dict, region_id)
    flood_fill((coord[0], coord[1] + 1), disk, region_dict, region_id)
    flood_fill((coord[0], coord[1] - 1), disk, region_dict, region_id)


def load_disk_data(run_str):
    f = open('day14data\\' + run_str + '.txt', 'r')

    return [line.strip('\n') for line in f.readlines()]


if __name__ == '__main__':
    # run = 'TEST'
    run = 'PUZZLE_INPUT'

    # compute_hashes_and_save()
    disk_data = populate_disk(load_disk_data(run))
    find_regions(disk_data)
