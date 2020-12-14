# https://adventofcode.com/2020/day/13

from itertools import count

def parse(raw):
    buses = map(int, raw.replace('x', '0').split(','))
    return [(mod, -i % mod) for i, mod in enumerate(buses) if mod]

def earliest_bus(start, buses):
    return next(
        bus * (i - start)
        for i in count(start)
        for bus, _ in buses
        if not i % bus
    )

def chinese_remainder(mods_rems):
    # from sympy.ntheory.modular import crt
    # return crt(*zip(*mods_rems))[0]

    def rem_indicator(mod_rem):
        mod, rem = mod_rem
        other_mods = prod // mod
        om_inv = pow(other_mods, mod-2, mod) # Euler's totient theorem
        indicator = other_mods * om_inv # act as bool(current mod)
        return rem * indicator

    import math
    prod = math.prod(m for m, _ in mods_rems)
    return sum(map(rem_indicator, mods_rems)) % prod

if __name__ == '__main__':
    assert earliest_bus(939, parse('7,13,x,x,59,x,31,19')) == 295
    assert chinese_remainder(parse('7,13,x,x,59,x,31,19')) == 1068781
    assert chinese_remainder(parse('17,x,13,19')) == 3417
    assert chinese_remainder(parse('67,7,59,61')) == 754018
    assert chinese_remainder(parse('67,x,7,59,61')) == 779210
    assert chinese_remainder(parse('67,7,x,59,61')) == 1261476
    assert chinese_remainder(parse('1789,37,47,1889')) == 1202161486
    buses = parse(open('data/day13.in').read())
    print(earliest_bus(1001612, buses))
    print(chinese_remainder(buses))