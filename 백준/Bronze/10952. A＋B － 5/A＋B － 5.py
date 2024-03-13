list = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    list.append(a + b)
for i in list:
    print(i)