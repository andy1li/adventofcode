# https://adventofcode.com/2019/day/16

import numpy as np

def parse(data):
    return np.fromiter(data, int, len(data))

def get_pattern(n):
    matrix = np.zeros([n, n], dtype=int)
    wave = [0, 1, 0, -1]
    for i in range(n):
        repeated = np.repeat(wave, i+1)
        pattern = np.tile(repeated, n//len(repeated)+1)
        matrix[i] = pattern[1:n+1]
    return matrix

def get_num(signal, n=8):
    return ''.join(map(str, signal[:n]))

def fft(signal, num_phases=100): 
    pattern = get_pattern(len(signal))
    if len(signal) == 8: print(pattern)

    for _ in range(num_phases):
        signal = abs(pattern @ signal) % 10

    return get_num(signal)

def trick_fft(signal, num_phases=100):
    signal = np.tile(signal, 10000)
    skip = int(get_num(signal, 7))
    signal = signal[skip:]

    for _ in range(num_phases):
        signal = np.cumsum(signal[::-1]) 
        signal = signal[::-1] % 10

    return get_num(signal)

if __name__ == '__main__':
    assert fft(parse('12345678'), 4) == '01029498'    
    assert fft(parse('80871224585914546619083218645595')) == '24176176'
    assert fft(parse('19617804207202209144916044189917')) == '73745418'
    assert fft(parse('69317163492948606335995924319873')) == '52432133'

    assert trick_fft(parse('03036732577212944063491565474664')) == '84462026'
    assert trick_fft(parse('02935109699940807407585447034323')) == '78725270'
    assert trick_fft(parse('03081770884921959731165446850517')) == '53553731'

    signal = parse(open('data/day16.in').read())
    print(fft(signal))
    print(trick_fft(signal))

