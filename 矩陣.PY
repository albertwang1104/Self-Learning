def turn(a:list):
    return [ i for i in reversed(a) ]

def rotate(a:list) -> list:
    b = [ [ 0 for i in range(len(a)) ] for j in range(len(a[0]))]
    for i in range(len(a[0])):
        for j in range(len(a)):
            b[i][j] = a[j][i]
    return [ i for i in reversed(b) ]

list1 = []
list2 = []

row, column, m = map(int, input().split())
for i in range(row):
    list1.append(list(map(int, input().split())))
action = list(map(int, input().split()))
 
for i in reversed(action):
    if i == 0:
        list2 = rotate(list1)
    else:
        list2 = turn(list1)
    list1 = list2    

print(len(list2), len(list2[0]))

for i in list2:
    for j in i:
        print(j, end = ' ')
    print()    