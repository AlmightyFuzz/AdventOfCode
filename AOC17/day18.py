import queue
import threading

TEST = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''

QUEUE_1 = queue.Queue()
QUEUE_2 = queue.Queue()

COUNT = 0


def duet(instructions):
    registers = {x: 0 for x in 'abcdefghijklmnopqrstuvwxyz'}
    sound = 0
    recovered_freq = 0

    idx = 0

    while idx < len(instructions):

        instr = instructions[idx][:3]
        reg = instructions[idx][4]
        val_str = instructions[idx][6:]

        if val_str is not '':
            try:
                val = int(val_str)
            except ValueError:
                val = registers[val_str]

        if instr == 'snd':
            sound = registers[reg]

        elif instr == 'set':
            registers[reg] = val

        elif instr == 'add':
            registers[reg] += val

        elif instr == 'mul':
            registers[reg] *= val

        elif instr == 'mod':
            registers[reg] %= val

        elif instr == 'rcv':
            if registers[reg] is not 0:
                recovered_freq = sound
                break

        if instr == 'jgz':
            if registers[reg] > 0:
                idx += val
            else:  # register <= 0
                idx += 1
        else:
            idx += 1

    print('Recovered sound: ', recovered_freq)


def duet2(instructions, p_id):
    '''
    Each of the two programs will be run in a seperate thread, with the two of them
    sending and receiving to two seperate queues. When both queues are empty then
    the program is done.s
    '''
    registers = {x: 0 for x in 'abcdefghijklmnopqrstuvwxyz'}
    registers['1'] = 1  # To deal with case 'jgz 1 3'
    registers['p'] = p_id

    idx = 0

    while idx < len(instructions):

        instr = instructions[idx][:3]
        reg = instructions[idx][4]
        val_str = instructions[idx][6:]
        val = 0

        if val_str is not '':
            try:
                val = int(val_str)
            except ValueError:
                val = registers[val_str]

        if instr == 'snd':
            if p_id == 0:
                QUEUE_2.put(registers[reg])
            if p_id == 1:
                QUEUE_1.put(registers[reg])

                global COUNT
                COUNT += 1

        elif instr == 'set':
            registers[reg] = val

        elif instr == 'add':
            registers[reg] += val

        elif instr == 'mul':
            registers[reg] *= val

        elif instr == 'mod':
            registers[reg] %= val

        elif instr == 'rcv':
            try:
                if p_id == 0:
                    registers[reg] = QUEUE_1.get(True, 3)  # seconds
                    QUEUE_1.task_done()

                if p_id == 1:
                    registers[reg] = QUEUE_2.get(True, 3)  # seconds
                    QUEUE_2.task_done()

            except queue.Empty:
                # The thread has been waiting for 3 seconds, so its queue is empty which
                # probably means that that other thread has finished.
                break

        if instr == 'jgz':
            if registers[reg] > 0:
                idx += val
            else:  # register <= 0
                idx += 1
        else:
            idx += 1

    print('Done')


def load_puzzle():
    return [x.strip('\n') for x in open('day18input.txt', 'r').readlines()]


if __name__ == '__main__':
    #IN_DATA = TEST.split('\n')
    IN_DATA = load_puzzle()

    # duet(IN_DATA)

    thing1 = threading.Thread(target=duet2, args=(IN_DATA, 0))
    thing2 = threading.Thread(target=duet2, args=(IN_DATA, 1))

    thing1.start()
    thing2.start()

    thing1.join()
    thing2.join()

    print('Count:', COUNT)
