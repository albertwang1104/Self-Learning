while True:
    try:
        y = int(input(''))
    except:
        break
    
    if y % 400 == 0:
        print('閏年')
    elif y % 100 == 0:
        print('平年')
    elif y % 4 == 0:
        print('閏年')
    else:
        print('平年')
