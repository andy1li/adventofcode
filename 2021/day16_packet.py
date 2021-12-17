# https://adventofcode.com/2021/day/16

from itertools import islice, chain
from collections import namedtuple
from math import prod

Packet = namedtuple('Packet', 'version, type, payload')

def to_bin(raw):
    return ''.join(bin(int(x, 16))[2:].zfill(4) for x in raw)

def read(stream, n):
    return ''.join(islice(stream, n))

def read_int(stream, n):
    return int(read(stream, n), 2)

def peek(stream):
    try:
        first = next(stream)
    except StopIteration:
        return None
    return chain([first], stream)

def parse(stream):
    if type(stream) == str: stream = iter(to_bin(stream))

    version, type_ = read_int(stream, 3), read_int(stream, 3)

    if type_ == 4:
        value, cont = '', True
        while cont:
            bits = read(stream, 5)
            cont = int(bits[0])
            value += bits[1:]
        return Packet(version, type_, int(value, 2))
    else:
        len_type, payload = int(next(stream)), tuple()
        if len_type == 0:
            stream = iter(read(stream, read_int(stream, 15)))
            while stream:
                payload += parse(stream),
                stream = peek(stream)
        elif len_type == 1:
            for _ in range(read_int(stream, 11)):
                payload += parse(stream),
        return Packet(version, type_, payload)

def sum_verison(packet):
    return packet.version + (
        0 if type(packet.payload) == int else 
        sum(map(sum_verison, packet.payload))
    )

def run(packet):
    if packet.type == 0: return sum(map(run, packet.payload))
    if packet.type == 1: return prod(map(run, packet.payload))
    if packet.type == 2: return min(map(run, packet.payload))
    if packet.type == 3: return max(map(run, packet.payload))
    if packet.type == 4: return packet.payload
    if packet.type == 5: return int(run(packet.payload[0]) > run(packet.payload[1]))
    if packet.type == 6: return int(run(packet.payload[0]) < run(packet.payload[1]))
    if packet.type == 7: return int(run(packet.payload[0]) == run(packet.payload[1]))

if __name__ == '__main__':
    assert sum_verison(parse('8A004A801A8002F478')) == 16
    assert sum_verison(parse('620080001611562C8802118E34')) == 12
    assert sum_verison(parse('C0015000016115A2E0802F182340')) == 23
    assert sum_verison(parse('A0016C880162017C3686B18A3D4780')) == 31
    assert run(parse('C200B40A82')) == 3
    assert run(parse('04005AC33890')) == 54
    assert run(parse('880086C3E88112')) == 7
    assert run(parse('CE00C43D881120')) == 9
    assert run(parse('D8005AC2A8F0')) == 1
    assert run(parse('F600BC2D8F')) == 0
    assert run(parse('9C005AC2F8F0')) == 0
    assert run(parse('9C0141080250320F1802104A08')) == 1

    packet = parse(open('data/day16.in').read().strip())
    print(sum_verison(packet))
    print(run(packet))
