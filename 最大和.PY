n,m = map(int, input('').split(' '))
list1 = []
for i in range(n):
    list1.append(list(map(int, input('').split(' '))))
    
max = 0 
for i in list1:
    i.sort()
    
for i in range(len(list1)):
    max += list1[i][-1]
    
print(max)

num = []
for i in range(len(list1)):
    if max % list1[i][-1] == 0:
        num.append(list1[i][-1])

if num == []:
    print('-1')
else:    
    for i in num :
        print(i, end = ' ')
