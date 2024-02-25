source = []
cnt = 0
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    source.append([a, b])
    cnt+=1

for i in source:
    print(sum(i))