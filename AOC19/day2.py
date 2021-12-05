TEST_1 = "1,0,0,0,99"
RESULT_1 = "2,0,0,0,99"

TEST_2 = "2,3,0,3,99"
RESULT_2 = "2,3,0,6,99"

TEST_3 = "2,4,4,5,99,0"
RESULT_3 = "2,4,4,5,99,9801"

TEST_4 = "1,1,1,4,99,5,6,0,99"
RESULT_4 = "30,1,1,4,2,5,6,0,99"


class ProgIndex(object):
    def __init__(self, start_index, max_index):
        self._current_index = start_index
        self._max_index = max_index

    @property
    def opcode_idx(self):
        return self._current_index

    @opcode_idx.setter
    def opcode_idx(self, new_idx):
        if new_idx > self._max_index:
            self._current_index = 0
        else:
            self._current_index = new_idx

    @property
    def input_A(self):
        idx = self._current_index + 1
        return self._validate(idx)

    @property
    def input_B(self):
        idx = self._current_index + 2
        return self._validate(idx)

    @property
    def output(self):
        idx = self._current_index + 3
        return self._validate(idx)

    def _validate(self, idx):
        if idx > self._max_index:
            return 0
        else:
            return idx


def process(program):
    idx = ProgIndex(0, len(program) - 1)

    while(True):
        op = program[idx.opcode_idx]
        a = program[idx.input_A]
        b = program[idx.input_B]
        out = program[idx.output]

        if op == 1:
            program[out] = program[a] + program[b]
        elif op == 2:
            program[out] = program[a] * program[b]
        elif op == 99:
            break

        idx.opcode_idx += 4

    return program


def get_puzzle_input():
    with open('InputData/day2Input.txt', 'r') as file:
        file_data = [line.strip('\n') for line in file]

        return [int(x) for x in file_data[0].split(',')]


if __name__ == "__main__":
    #program = [int(x) for x in TEST_1.split(',')]
    #program = [int(x) for x in TEST_2.split(',')]
    #rogram = [int(x) for x in TEST_3.split(',')]
    #program = [int(x) for x in TEST_4.split(',')]

    program = get_puzzle_input()
    program[1] = 12
    program[2] = 2

    result = process(program)
    print(result[0])
