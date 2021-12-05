TEST1 = [0, 2, 7, 0]
PUZZLE_INPUT = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]


def infin_loop_spotter(memory_banks):
    cycles = 0
    previous_configs = []
    # list(listA) creates a shallow copy
    previous_configs.append(list(memory_banks))

    first_repeated_config = []
    loop_size = 0

    while True:

        # find largest value in list
        largest = max(memory_banks)
        large_idx = memory_banks.index(largest)
        memory_banks[large_idx] = 0

        # Distribute the blocks amongst the banks
        idx = large_idx
        for i in range(largest):
            idx += 1
            if idx >= len(memory_banks):
                idx = 0

            memory_banks[idx] += 1

        if first_repeated_config == []:
            # if we haven't found a repeating configuration
            cycles += 1

            # Check if current configuration of memory blocks has been seen before
            if memory_banks in previous_configs:
                first_repeated_config = list(memory_banks)
                # break
            else:
                previous_configs.append(list(memory_banks))
        else:
            # If we have found a repeated config, keep looking until we find it again
            # to find the size of the repeating loops
            loop_size += 1

            if memory_banks == first_repeated_config:
                break

    return cycles, loop_size


if __name__ == '__main__':
    # print(infinLoopSpotter(TEST1))
    print(infin_loop_spotter(PUZZLE_INPUT))
