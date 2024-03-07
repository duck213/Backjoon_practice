import sys
a,b = map(int,input().split())
basket = [0]*a
for _ in range(b):
    c,d,e = map(int, sys.stdin.readline().split())
    for i in range(c-1,d):
        basket[i] = e
print(*basket)