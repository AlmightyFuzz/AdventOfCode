import re

test_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

test_data_invlaid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

test_data_valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

def check_passports(passports):
    valid_passports = 0

    for passport_data in passports:
        passport_data = passport_data.replace('\n', ' ')
        passport_data = passport_data.strip(' ')

        fields = [field for field in passport_data.split(' ')]
        kv_pairs = [pair.split(':') for pair in fields]

        passport = {pair[0]: pair[1] for pair in kv_pairs}

        if validate(passport):
            valid_passports +=1

    return valid_passports


def validate(passport):
    req_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}  # "cid" optional

    if "cid" in passport:
        passport.pop("cid")

    if passport.keys() != req_fields: return False
    if not (1920 <= int(passport["byr"]) <= 2002): return False
    if not (2010 <= int(passport["iyr"]) <= 2020): return False
    if not (2020 <= int(passport["eyr"]) <= 2030): return False
    if not (len(passport["pid"]) == 9): return False
    if not (passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}): return False
    if not (re.fullmatch(r"#[0-9a-f]{6}", passport["hcl"])) : return False

    height = passport["hgt"]
    if not (re.fullmatch(r"\d+(cm|in)", height)): return False
    if height.endswith("cm") and not (150 <= int(height[:-2]) <= 193): return False
    if height.endswith("in") and not(59 <= int(height[:-2]) <= 76): return False

    # if we've reached this far then the  passport is valid
    return True


def get_puzzle_input():
    with open('InputData/day4.txt', 'r') as file:
        return file.read()


if __name__ == '__main__':
    #passports = test_data.split('\n\n')
    #passports = test_data_invlaid.split('\n\n')
    #passports = test_data_valid.split('\n\n')

    passports = get_puzzle_input().split('\n\n')

    num = check_passports(passports)
    print(num)