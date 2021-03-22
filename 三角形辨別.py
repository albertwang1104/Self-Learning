try:
    triangle = list(map(int, input('').split(' ')))
    triangle.sort()
    
    if triangle[0] + triangle[1] <= triangle[2]:
        print(triangle[0], triangle[1], triangle[2])
        print('No')
        if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
            print(triangle[0], triangle[1], triangle[2])
            print('Right')
        elif triangle[0]**2 + triangle[1]**2 < triangle[2]**2:
            print(triangle[0], triangle[1], triangle[2])
            print('Acute')
        else:
            print(triangle[0], triangle[1], triangle[2])
            print('Obtuse')
except:
    pass