n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    
    if (lst[1] - lst[0]) == (lst[3] - lst[2]): #是否為等差數列
        lst.append(lst[3] + (lst[1] - lst[0]))
    
    elif (lst[1] / lst[0]) == (lst[3] / lst[2]): #是否為等比數列
        lst.append(lst[3] * (lst[1] // lst[0]))
    
    for i in lst:
        print(i, end = ' ')
    print()














