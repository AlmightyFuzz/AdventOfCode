'''
Converts the string into a list of sorted words. This puts duplicate entries
next to each other, so just compare adjacent entries
'''

TEST1 = 'aa bb cc dd ee'
TEST2 = 'aa bb cc dd aa'
TEST3 = 'aa bb cc dd aaa'
TEST4 = 'aa bb cc dd aaa cc'

TEST5 = 'abcde fghij'
TEST6 = 'abcde xyz ecdab'
TEST7 = 'a ab abc abd abf abj'
TEST8 = 'iiii oiii ooii oooi oooo'
TEST9 = 'oiii ioii iioi iiio'


def passphrase_check(phrase):
    words = phrase.strip('\n')
    words = words.split(' ')

    # Sort letters in a word into order in order to find anagrams
    words = list(map(sort_word, words))

    words = sorted(words)

    for i, word in enumerate(words):
        if i + 1 < len(words):
            if word == words[i + 1]:
                return False

    return True

# Sorts all the letters in a given word into alphabetical order


def sort_word(word):
    letters = list(word)
    letters = sorted(letters)
    sorted_word = ''.join(letters)

    return sorted_word


def process_file():
    puzzle_input = open('day4input.txt', 'r')
    valid_phrases = 0

    for line in puzzle_input:
        if passphrase_check(line):
            valid_phrases += 1

    print("Valid phrases: {0}".format(valid_phrases))


if __name__ == '__main__':
    process_file()

    # print(passphraseCheck(TEST1))
    # print(passphraseCheck(TEST2))
    # print(passphraseCheck(TEST3))
    # print(passphraseCheck(TEST4))

    # print(passphraseCheck2(TEST6))
