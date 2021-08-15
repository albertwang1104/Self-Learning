def rotate(a:list) -> list:
    b = [ [ 0 for i in range(len(a)) ] for j in range(len(a[0]))]
    for i in range(len(a[0])):
        for j in range(len(a)):
            b[i][j] = a[j][i]
    return b

r, c = map(int, input().split())
lst = []
for i in range(r):
    lst.append(list(map(int, input().split())))
        
for i in rotate(lst):
    for j in i:
        print(j, end = " ")
    if j != lst[r-1][c-1]:
        print()
    else:
        break

