a,b = map(int,input().split())
x_a, x_b = [],[]
for i in range(a):
    ele = list(map(int, input().split()))
    x_a.append(ele)
for j in range(a):
    eles = list(map(int, input().split()))
    x_b.append(eles)

for c in range(a):
    ka = []
    for d in range(b):
        exp = x_a[c][d]+x_b[c][d]
        ka.append(exp)
    print(*ka)