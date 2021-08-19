a, b = map(int, input().split())
ans = []

for i in range(a, b):
    arm = list(str(i))
    num = 0
    for j in arm:
        num += int(j)**len(arm)
    if num == i:
        ans.append(i)
    else:
        continue
        

if ans == []:
    print('none')
else:
    for i in range(len(ans)):
        print(ans[i], end = ' ')

'''找出範圍的armstrong number
for i in range(1000000):
    ax = list(str(i))
    num = 0
    for j in ax:
        num += int(j)**len(ax)
    if num == i:
        print(i)
        ans.append(num)
    ax = []
print(ans)
'''

'''
法一：list comprehension + sum(map()) (0.4s = 400ms)


ans = [

    k

    for k in map(str, range(*map(int, input().split())))

    if int(k) == sum(map(lambda x:int(x)**len(k), k))

]

print(*ans, 'none'*(not ans))

'''
'''法二
from bisect import bisect_left, bisect_right

ans = (1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084)

n, m = map(int, input().split())

s = ans[bisect_left(ans, n):bisect_right(ans, m)]

print(*s, 'none'*(not s))
'''


