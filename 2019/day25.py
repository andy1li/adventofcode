# https://adventofcode.com/2019/day/25

from collections import deque
from intcode import run
from itertools import chain, combinations

DIRECTION = { 'n': 'north', 's': 'south', 'w': 'west',  'e': 'east' }

class Agent:
    def __init__(self):
        self.tasks = []
        self.command_queque = deque([
            'south', 'east', 'take whirled peas', 'west', 'north', 'north',
            'east', 'take ornament', 'north', 'north', 'take dark matter', 
            'south', 'south', 'west', 'west', 'west', 'take candy cane',
            'west', 'west', 'take tambourine', 'east', 'east', 'east', 'north', 
            'take astrolabe', 'east', 'take hologram', 'east', 'take klein bottle',
            'west', 'south', 'west'
        ])

    @property
    def is_running(self):
        return self.tasks or self.command_queque

    def next_command(self, prompt, new_task=None):
        if new_task == 'hack': 
            self.tasks.extend(['check', 'adjust_inventory', 'check_inventory'])
        if not self.command_queque: self.perform_tasks(prompt)
        return self.command_queque.popleft()

    def check_inventory(self, prompt):
        if 'Items in your inventory' in prompt:
            self.inventory = { 
                line[2:]
                for line in prompt.splitlines()
                if line.startswith('- ')
            }
            all_items = self.inventory.copy()
            self.powerset = chain.from_iterable(
                combinations(all_items, i)
                for i in range(len(self.inventory)+1)
            )
            self.tasks.pop()
            print(self.inventory, '\n')
            if self.tasks: self.perform_tasks()
        else:
            self.command_queque.append('inv')

    def adjust_inventory(self, _):
        target_items = set(next(self.powerset))
        if target_items != self.inventory:
            drops = self.inventory - target_items
            takes = target_items - self.inventory
            for drop in drops:
                self.command_queque.append('drop ' + drop)
                self.inventory.discard(drop)
            for take in takes:
                self.command_queque.append('take ' + take)
                self.inventory.add(take)

        self.command_queque.append('north')
        self.tasks.pop()

    def check(self, prompt):
        if 'Alert!' in prompt:
            self.tasks.append('adjust_inventory')
            self.perform_tasks(prompt)

    def perform_tasks(self, prompt=''):
        if not self.tasks: return
        task = self.tasks[-1]
        getattr(self, task)(prompt)
        
def read(stream, buffer = ''):
    for x in map(chr, stream):
        buffer += x
        if buffer.endswith('Command?\n'):
            yield buffer     
            buffer = ''
    else:
        print(buffer.strip()); return

def repl(code):
    commands, agent = [], Agent()
    
    for prompt in read(run(code, commands)):
        print(prompt.strip())

        if agent.is_running:
            command = agent.next_command(prompt)
            print('❯ ' + command + '\n')
        else:
            command = input('❯ '); print()
            if command in DIRECTION: command = DIRECTION[command]
            if command == 'hack':
                command = agent.next_command(prompt, 'hack')
                print('❯ ' + command + '\n')

        commands.extend(command.encode() + b'\n')

if __name__ == '__main__':
    code = [*map(int, open('data/day25.in').read().split(','))]
    repl(code)