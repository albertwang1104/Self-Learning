a, b, c = map(int, input().split(' '))

if a > 0:
    a = 1
if b > 0:
    b = 1
    
if a & b == c:
    print('AND')
if a | b == c:
    print('OR')
if a ^ b == c:
    print('XOR')
if a & b != c and a | b != c and a ^ b != c:
    print('IMPOSSIBLE')
