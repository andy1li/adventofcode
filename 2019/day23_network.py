# https://adventofcode.com/2019/day/23

from collections import deque
from intcode import run

class NIC:
    def __init__(self, address):
        self.queue = deque([address])
        self.empty_calls = 0

    def __iter__(self): return self

    def __next__(self):
        if self.queue: 
            self.empty_calls = 0
            return self.queue.popleft()
        else:
            self.empty_calls += 1
            return -1 

    @property
    def is_idle(self):
        return not self.queue and self.empty_calls > 1
    
def run_network(code): 
    def router(packet):
        global NAT
        dest, x, y = packet

        if dest == 255:
            NAT = x, y
            if not previous_NAT: print('NAT receives:', y)
        else: 
            network[dest].queue.extend([x, y])
    
    previous_NAT = None
    network = [*map(NIC, range(50))]
    computers = [run(code, network[i], router) for i in range(50)]
    while True: 
        for i in range(50): 
            if not network[i].is_idle: next(computers[i])

        if all(network[i].is_idle for i in range(50)):
            network[0].queue.extend(NAT)
            if NAT == previous_NAT: 
                print('NAT sends:', NAT[1]); break
            previous_NAT = NAT

if __name__ == '__main__':
    code = [*map(int, open('data/day23.in').read().split(','))]
    run_network(code)