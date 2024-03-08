import sys
n = int(input())
for _ in range(n):
    c = sys.stdin.readline()
    print(c[0]+c[-2])