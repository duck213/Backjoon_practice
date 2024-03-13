n = int(input())
list = [[int(k) for k in input().split()] for i in range(n)]
for j in range(n):
    print(sum(list[j]))


