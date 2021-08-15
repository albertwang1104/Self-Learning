while True:
    try:
        ans = input().split()
        print(eval(''.join(ans)))
    except:
        break
