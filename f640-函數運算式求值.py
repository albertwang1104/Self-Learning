def f(x: int):  return 2*x - 3

def g(x: int, y: int):  return 2*x + y - 7

def h(x: int, y: int, z: int):  return 3*x - 2*y + z

stack = []
getn = stack.pop

for sym in reversed(input().split()):
    stack.append(
        f(getn()) if sym == "f"
        else g(getn(), getn()) if sym == "g"
        else h(getn(), getn(), getn()) if sym == "h"
        else int(sym)
        )
    
print(getn())