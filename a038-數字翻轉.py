n = list(input())
if n[0] == '0':
    print('0')
    pass
else:
    while True:
        if n[-1] != '0':
            print(''.join(n[::-1]))
            break
        else:
            n.pop()
    
