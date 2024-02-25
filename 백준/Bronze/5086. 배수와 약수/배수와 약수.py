source = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif a <= b and b%a == 0:
        source.append("factor")
    elif a > b and a%b == 0:
        source.append("multiple")
    elif a%b != 0 and b%a != 0:
        source.append("neither")
for i in source:
    print(i)