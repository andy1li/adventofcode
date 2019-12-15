'#ip 5'
0  addi 5 16 5  jmp 17 '-> init'

'start:'
1  seti 1 _ 3   r3 = 1
2  seti 1 _ 2   r2 = 1

'loop:'
3  mulr 2 3 4   r4 = r2 * r3
eqrr 1 4 4   'if r1 == r2 * r3:'
5  addr 5 4 5   True:  jmp 7 '-> ans += r3'
addi 5 1 5   False: jmp 8 '-> r2++'
7  addr 0 3 0   r0 += r3 'ans += r3'

'r2++:'
8  addi 2 1 2   r2++
9  gtrr 2 1 4   'if r2 > r1:' 
10 addr 5 4 5   True:  jmp 12 '-> r3++'
11 seti 2 _ 5   False: jmp 3 'while r2 <= r1: -> loop'

'r3++:'
12 addi 3 1 3   r3++
gtrr 3 1 4   'if r3 > r1:' 
addr 5 4 5   True:  jmp 16 '-> halt'
15 seti 1 _ 5   False: jmp 2 'while r3 <= r1: r2 = 1; -> loop'

'halt:'
16 mulr 5 5 5   jmp 257 

'init: [0, 1010, 0, 0, _, 1]'
17 addi 1 2 1   r1 +=  2
mulr 1 1 1   r1 **= 2
19 mulr 1 5 1   r1 *= 19
muli 1 11 1  r1 *= 11

addi 4 7 4   r4 +=  7
22 mulr 4 5 4   r4 *= 22
addi 4 20 4  r4 += 20
addr 1 4 1   r1 += r4 'r1 = 1010'

25 addr 5 0 5   if  r0: jmp 27 '-> init extra'
seti 0 _ 5   if !r0: jmp  1 '-> start'

'init extra: [0, 10551410, 0, 0, _, 1]'
27 setr 5 _ 4   r4 =  27
28 mulr 4 5 4   r4 *= 28
29 addr 4 5 4   r4 += 29
30 mulr 4 5 4   r4 *= 30
muli 4 14 4  r4 *= 14
32 mulr 4 5 4   r4 *= 32
addr 1 4 1   r1 += r4 'r1 = 10551410'

seti 0 _ 0   r0 = 0 'ans = 0'
seti 0 _ 5   jmp 1  '-> start'