'#ip 5'
0  seti 123 _ 4  'r4 = 123'

'check:'
1  bani 4 456 4  'r4 &= 456'
2  eqri 4  72 4  'if r4 == 72:'
3  addr 5   4 5  True:  jmp 5 '-> r4 = 0; start'
4  seti 0   _ 5  False: jmp 1 '-> check'
5  seti 0        _ 4  'r4 = 0'

'while r0 != r4:'
6  bori 4    65536 1  r1 = r4 | 65536 'r1 set bit 16'
7  seti 2024736  _ 4                  'r4 = 2024736'

'while r1 >= 256:' #  r1, x = divmod(r1, 256)
8  bani 1      255 2  r2 = r1 & 255  'r2 = mod(r1, 256)'
9  addr 4        2 4                 'r4 += r2'
10 bani 4 16777215 4  r4 &= 16777215 'r4 %= 16777216'
11 muli 4 65899    4                 'r4 *= 65899 '
12 bani 4 16777215 4  r4 &= 16777215 'r4 %= 16777216'

13 gtir 256      1 2  'if r1 < 256:'
14 addr 5        2 5  True:  jmp 16 (28) '-> check r4 == r0?'
15 addi 5        1 5  False: jmp 17      '-> clear r2'

; 'check r4 == r0?:'
; 16 seti 27       _ 5  jmp 28 '-> check r4 == r0?'

'clear r2:'
17 seti 0   _ 2  'r2 = 0'

'while ((r2 + 1) * 256) <= r1:' # r1 = div(r1, 256)
18 addi 2   1 3  'r3 = r2 + 1'
19 muli 3 256 3  'r3 *= 256'

20 gtrr 3   1 3  'if r3 > r1:'
21 addr 5   3 5  True:  jmp 23 (26) '-> r1 = r2; -> while r1 >= 256'
22 addi 5   1 5  False: jmp 24      '-> r2++'

; 'r1 = r2 + r3:'
; 23 seti 25  _ 5  jmp 26 '-> r1 = r2 + r3'

'r2++:'
24 addi 2   1 2  'r2++'
25 seti 17  _ 5  jmp 18 '-> while ((r2 + 1) * 256) <= r1'

'r1 = r2 + r3:'
26 setr 2   _ 1  'r1 = div(r1, 256)'
27 seti 7   _ 5  jmp 8 '-> while r1 >= 256'

'check r4 == r0?:'
28 eqrr 4   0 2   'if r4 == r0:'
29 addr 5   2 5   True:  jmp +r2 'halt'
30 seti 5   _ 5   False: jmp 6 '-> while r0 != r4'