'''
10
0 11 22 33 55 66 77 99 88 44

1
13

2
73 65
'''
a = int(input())
score = list(map(int, input().split()))
score.sort()

for i in score:
    print(i, end = ' ')
print()    

for i in reversed(score):
    if i < 60:
        print(i)
        break
    if i == score[0] :
        print('best case')

for i in score:
    if i >= 60:
        print(i)
        break
    if i == score[-1] :
        print('worst case')

        
