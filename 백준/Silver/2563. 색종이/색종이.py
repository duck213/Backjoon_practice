n = int(input())
collect = []
for _ in range(n):
    a,b = map(int,input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            if [i, j] not in collect:
                collect.append([i, j])
print(len(collect))