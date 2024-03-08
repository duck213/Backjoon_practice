import sys
n = int(input())
c = sys.stdin.readline()
a = [int(i) for i in list(c[:-1])]
print(sum(a))