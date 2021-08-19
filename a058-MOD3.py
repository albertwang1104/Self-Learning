n = int(input())
num = [int(input()) for i in range(n)]
a = 0
b = 0
c = 0
for i in num:
    if i % 3 == 0:
        a += 1
    elif i % 3 == 1:
        b += 1
    else:
        c += 1

print(a, b, c)
