# https://adventofcode.com/2019/day/16

from itertools import chain, cycle, islice, repeat
import numpy as np

def parse(data):
    return np.fromiter(map(int, data), dtype=np.int8)

def get_pattern(n):
    pattern = np.zeros([n, n], dtype=np.int8)
    for i in range(n):
        row = cycle(chain(
            repeat(0, i+1), repeat(1, i+1), 
            repeat(0, i+1), repeat(-1, i+1)
        ))
        pattern[i] = np.fromiter(islice(row, n+1), np.int8)[1:]
    return pattern

def fft(signal, num_phases=100): 
    pattern = get_pattern(len(signal))
    if len(signal) == 8: print(pattern)

    for _ in range(num_phases):
        signal = abs(pattern @ signal) % 10

    return ''.join(map(str, signal[:8]))

def trick_fft(signal, num_phases=100):
    signal = np.tile(signal, 10000)
    offset = int(''.join(map(str, signal[:7])))
    signal = signal[offset:]

    for _ in range(num_phases):
        rev = signal[::-1]
        signal = np.cumsum(rev)[::-1]
        signal %= 10

    return ''.join(map(str, signal[:8]))

if __name__ == '__main__':
    assert fft(parse('12345678'), 4) == '01029498'    
    assert fft(parse('80871224585914546619083218645595')) == '24176176'
    assert fft(parse('19617804207202209144916044189917')) == '73745418'
    assert fft(parse('69317163492948606335995924319873')) == '52432133'

    assert trick_fft(parse('03036732577212944063491565474664')) == '84462026'
    assert trick_fft(parse('02935109699940807407585447034323')) == '78725270'
    assert trick_fft(parse('03081770884921959731165446850517')) == '53553731'

    signal = [*map(int, open('data/day16.in').read())]
    print(fft(signal))
    print(trick_fft(signal))

