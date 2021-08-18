ans = list(input())
'''
right = []
left = []

if len(ans) % 2 == 0:
    j = len(ans)//2
else:
    j = len(ans)//2 + 1
    
for i in range(len(ans)//2-1, -1, -1):
    right.append(ans[i])
    left.append(ans[j])
    j += 1
    
j = 0
for i in range(len(right)):
    if right[i] != left[i]:
        print('no')
        break
    else:
        j += 1
        continue
'''
re = [i for i in reversed(ans)]

j = 0
for i in range(len(re)):
    if re[i] != ans[i]:
        print('no')
        break
    else:
        j += 1
        continue
    
if j == len(ans):
    print('yes')

