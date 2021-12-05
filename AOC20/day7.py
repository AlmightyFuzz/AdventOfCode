import re
test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

def get_puzzle_input():
    with open("InputData/day7.txt") as file:
        return [line.strip('\n') for line in file]

def parse_rules(the_rules):
    rules = {}

    for line in the_rules:
        matches = re.match(r'(\w+ \w+) bags contain (.*)', line)
        bag_colour = matches.group(1)
        contents = matches.group(2)

        if contents == 'no other bags.':
            rules[bag_colour] = []
        else:
            matches = [re.match(r'(\d+) (\w+ \w+) bag(s?)', bag) for bag in contents.split(', ')]
            contents = [(int(match.group(1)), match.group(2)) for match in matches]

            rules[bag_colour] = contents
 
    return rules

def count_shiny_gold(rules):
    colours = rules.keys()
    num_gold = 0

    for colour in colours:
        if search_for_gold(colour, rules) == True:
            num_gold += 1

    return num_gold

def search_for_gold(colour, rules):
    if rules[colour] == []:
        return False

    contents_colours = [contents[1] for contents in rules[colour]]
    if 'shiny gold' in contents_colours:
        return True

    for contents in rules[colour]:
        if search_for_gold(contents[1], rules) == True:
            return True
        else:
            continue


if __name__ == "__main__":
    #input = test_data.split('\n')
    input = get_puzzle_input()

    rules = parse_rules(input)
    num = count_shiny_gold(rules)

    print(num)