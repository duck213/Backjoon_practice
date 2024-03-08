import sys
a,b = map(int,input().split())
basket = [i for i in range(1,a+1)]
for _ in range(b):
    c,d = map(int, sys.stdin.readline().split())
    tas = basket[c-1:d]
    tas = tas[::-1]
    cnt = 0
    for i in range(c-1,d):
        basket[i] = tas[cnt]
        cnt+=1
print(*basket)