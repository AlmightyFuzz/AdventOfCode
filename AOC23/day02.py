import common

TEST_DATA = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def find_possible_games(games):
    id_total = 0

    for game in games:
        game_data = game.split(': ')
        game_data[0] = game_data[0].split(' ')
        game_data[1] = game_data[1].split('; ')
        game_data[1] = [x.split(', ') for x in game_data[1]]
        
        game_valid = True

        for hand in game_data[1]:
            for cubes in hand:
                cubes = cubes.split(' ')
                if game_valid:
                    if (cubes[1] == "red" and int(cubes[0]) > 12) \
                    or (cubes[1] == "green" and int(cubes[0]) > 13) \
                    or (cubes[1] == "blue" and int(cubes[0]) > 14):
                        game_valid = False
                        break

        if game_valid:
            id = int(game_data[0][1])
            id_total += id

    return id_total

if __name__ == "__main__":
    #puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day02.txt")

    result = find_possible_games(puz_input)

    print(result)