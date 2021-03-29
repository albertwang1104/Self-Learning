try:
    triangle = list(map(int, input('').split(' ')))
    triangle.sort()
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    
    if a + b <= c:
        print(a, b, c)
        print('No')
    elif a**2 + b**2 == c**2:
        print(a, b, c)
        print('Right')
    elif a**2 + b**2 < c**2:
        print(a, b, c)
        print('Obtuse')
    else:
        print(a, b, c)
        print('Acute')
except:
    pass 