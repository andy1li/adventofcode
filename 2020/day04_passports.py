# https://adventofcode.com/2020/day/4

import re

def parse(batch):
    passports = batch.split('\n\n')
    parse_passport = lambda pairs: dict(pair.split(':') for pair in pairs)
    return [parse_passport(p.split()) for p in passports]

def validate(passport, strict):
    reqs = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} # 'cid' optional
    all_reqs = all(r in passport for r in reqs)
    if not strict: return all_reqs

    def validate_height(hgt):
        try: num, unit = int(hgt[:-2]), hgt[-2:]
        except ValueError: return False 
        return unit in {'cm', 'in'} \
        and (150 <= num <= 193 if unit == 'cm' else 59 <= num <= 76)

    return (
        all_reqs
    and 1920 <= int(passport['byr']) <= 2002
    and 2010 <= int(passport['iyr']) <= 2020
    and 2020 <= int(passport['eyr']) <= 2030
    and validate_height(passport['hgt'])
    and bool(re.match('^#[a-f0-9]{6}$', (passport['hcl'])))
    and passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    and bool(re.match('^[0-9]{9}$', (passport['pid'])))
    )

def count_valid(passports, strict=False): 
    return sum(validate(p, strict) for p in passports)

TEST = '''\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

INVALIDS ='''\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

VALIDS = '''\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

if __name__ == '__main__':
    assert count_valid(parse(TEST)) == 2
    assert count_valid(parse(INVALIDS), strict=True) == 0
    assert count_valid(parse(VALIDS), strict=True) == 4

    passports = parse(open('data/day04.in').read())
    print(count_valid(passports))
    print(count_valid(passports, strict=True))
