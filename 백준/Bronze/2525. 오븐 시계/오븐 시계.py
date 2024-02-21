a, b = map(int, input().split())
value = int(input())

if value >= 60:
    hour = value // 60
    min = value % 60
    a += hour
    b += min
else:
    b += value

if b > 59:
    a += 1
    b -= 60
if a > 23:
    a -= 24

print(a, b)