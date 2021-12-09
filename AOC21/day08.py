import common

TEST_DATA = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""
TEST_DATA2 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def parse_input(data):
    signals = [[output.split(' ') for output in line.split(' | ')]
               for line in data]

    return signals


def count_unique_signals(signals):
    unique_signals = 0
    outputs = [signal[1] for signal in signals]

    for output in outputs:
        if len(output) == 2:  # one
            unique_signals += 1
        elif len(output) == 4:  # four
            unique_signals += 1
        elif len(output) == 3:  # seven
            unique_signals += 1
        elif len(output) == 8:  # eight
            unique_signals += 1


if __name__ == "__main__":
    data = common.load_test_data(TEST_DATA)
    #data = common.load_puzzle_input("data/day08.txt")

    signals = parse_input(data)
    count_unique_signals(signals)

    print(data)
