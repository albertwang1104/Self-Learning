

'''
3 2 3
1, 1
3, 1
1, 2
1 0 0
'''

def turn(a:list):
    return [ i for i in reversed(a) ]

def rotate(a:list):
    b = [ i for i in reversed(a) ]
    b = [ a[j][i] for i in range(len(a[0])) for j in range(len(a)) ]
    b = [ list(b[0:len(a)]), list(b[len(a):len(a)*2]) ]
    return b

list1 = []
list2 = []

row, column, m = map(int, input().split())
for i in range(row + 1):
    list1.append(list(map(int, input().split())))
action = list(map(int, input().split()))
 
for i in reversed(action):
    if i == 0:
        list2 = rotate(list1)
    else:
        list2 = turn(list1)

print(len(list2), len(list2[0]))

for i in list2:
    for j in reversed(i):
        print(j, end = ' ')
    print()    