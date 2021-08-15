import sys

for s in sys.stdin:
    print(eval(s.replace("/", "//")))

while True:
    try:
        ans = input().split()
        print(eval(''.join(ans)))
    except:
        break
