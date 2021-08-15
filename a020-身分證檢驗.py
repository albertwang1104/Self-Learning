ID = {'A':10, 'J':18, 'S':26, 
        'B':11, 'K':19, 'T':27, 
        'C':12, 'L':20, 'U':28, 
        'D':13, 'M':21, 'V':29, 
        'E':14, 'N':22, 'W':32, 
        'F':15, 'O':35, 'X':30, 
        'G':16, 'P':23, 'Y':31, 
        'H':17, 'Q':24, 'Z':33, 
        'I':34, 'R':25, }


id = list(input(''))
ans = 0
t = 0

for i in range(len(id)+1):
    if i != 0:
        id[i] = int(id[i])
    else:
        id[0] = list(str(ID[id[0]]))
        for i in reversed(id[0]):
            id.insert(0, int(i))
        id.pop(2)

for i in range(len(id)):
    if i == 0:
        ans += id[i]
    else:
        ans += id[i] * (10-i)
ans += id[-1]

if ans % 10 == 0:
    print('real')
else:
    print('fake')

