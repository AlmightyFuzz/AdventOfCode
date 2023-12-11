import common

TEST_DATA = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def find_possible_games(games):
    id_total = 0
    power_total = 0

    for game in games:
        game_data = game.split(': ')
        game_data[0] = game_data[0].split(' ')
        game_data[1] = game_data[1].split('; ')
        game_data[1] = [x.split(', ') for x in game_data[1]]
        
        game_valid = True
        max_red = 0
        max_green = 0
        max_blue = 0

        for hand in game_data[1]:
            for cubes in hand:
                cubes = cubes.split(' ')

                num_cubes = int(cubes[0])
                    
                if cubes[1] == "red":
                    if num_cubes > 12:
                        game_valid = False

                    if num_cubes > max_red:
                        max_red = num_cubes

                elif cubes[1] == "green":
                    if num_cubes > 13:
                        game_valid = False

                    if num_cubes > max_green:
                        max_green = num_cubes

                elif cubes[1] == "blue":
                    if num_cubes > 14:
                        game_valid = False

                    if num_cubes > max_blue:
                        max_blue = num_cubes

        if game_valid:
            id = int(game_data[0][1])
            id_total += id

        power = (max_red * max_green * max_blue)
        power_total += power

    print(f"Sum of IDs for valid games: {id_total}")
    print(f"Sum of powers: {power_total}")

if __name__ == "__main__":
    #puz_input = common.load_test_data(TEST_DATA)
    puz_input = common.load_puzzle_input("data/day02.txt")

    find_possible_games(puz_input)