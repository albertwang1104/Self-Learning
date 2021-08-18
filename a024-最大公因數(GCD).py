def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())

if a < b:
    a, b = b, a
    ans = gcd(a, b)
else:
    ans = gcd(a, b)
    
print(ans)
