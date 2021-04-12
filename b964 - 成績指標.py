while True:
    try:
        a = int(input())
        score = list(map(int, input().split()))
        score.sort()
        
        for i in score:
            print(i, end = ' ')
        print()    
        
        for i in reversed(score):
            if i < 60:
                print(i)
                break
            if i == score[0] :
                print('best case')
                break
        
        for i in score:
            if i >= 60:
                print(i)
                break
            if i == score[-1] :
                print('worst case')
                break
    except Exception:
        pass            