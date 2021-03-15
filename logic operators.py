def logic(a,b,c):
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
'''
list1 = list(map(int, input().split(' ')))
a = list1[0]
b = list1[1]
c = list1[2]
logic(a,b,c)
'''

a, b, c = map(eval, input().split(' '))
print(type(a), type(b), type(c))
print(a, b, c)
logic(a,b,c)
