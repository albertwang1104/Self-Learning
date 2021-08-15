n = int(input())

d = {}
l = 0 #次方
i = 2 #因數

while n > 1:
    if n % i == 0:
        if i not in d:
            l = 1
            d[i] = l
        else:
            l += 1
            d[i] = l
        n //= i
        i = 2
    else:
        i += 1
        
x = 0
for k in d:
    x += 1
    if d[k] != 1:
        if x == len(d):
            print(f'{k}^{d[k]}')
        else:
            print(f'{k}^{d[k]}', end = " * ")
    else:
        if x == len(d):
            print(f'{k}')
        else:
            print(f'{k}', end = " * ")

