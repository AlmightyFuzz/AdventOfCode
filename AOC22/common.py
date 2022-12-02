def load_test_data(data):
    data = [line for line in data.split('\n')]
    return data

def load_puzzle_input(file):
    data = [line.strip('\n') for line in open(file)]
    return data