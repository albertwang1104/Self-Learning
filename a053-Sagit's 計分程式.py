while True:
    try:
        n = int(input())
        score = 0
        if n <= 10:
            score = n*6
        elif 10 < n <= 20:
            score = (n-10)*2 + 60
        elif 20 < n <= 40:
            score = n + 60
        elif n > 40:
            score = 100
        print(score)
    except:
        break


