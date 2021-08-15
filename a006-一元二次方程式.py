while True:
    try:        
        a, b, c = map(int, input().split())
    except:
        break
    
    d = b**2 - 4*a*c
    x1 = 0
    x2 = 0
    
    if d < 0:#無解
        print('No real root')
    elif d == 0:#重根
        x1 = int((-b + d**(1/2)) / (2*a))
        print(f'Two same roots x={x1}')
    else:#異根
        x1 = int((-b + d**(1/2)) / (2*a))
        x2 = int((-b - d**(1/2)) / (2*a))   
        print(f'Two different roots x1={x1} , x2={x2}')
        




