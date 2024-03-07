import sys
a,b = map(int,input().split())
basket = [i for i in range(1,a+1)]
for _ in range(b):
    c,d = map(int, sys.stdin.readline().split())
    basket[c-1], basket[d-1] = basket[d-1], basket[c-1]
print(*basket)