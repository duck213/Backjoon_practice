a, b, c = map(int, input().split())
value = int(input())
if value >= 86400:
    value %= 86400

if value >= 3600:
    hour = value // 3600
    min = value % 3600
    sec = min % 60
    min = min // 60
    a += hour
    b += min
    c += sec
elif 60 <= value < 3600:
    min = value // 60
    sec = value % 60
    b += min
    c += sec
else:
    c += value

if c > 59:
    b += 1
    c -= 60
if b > 59:
    a += 1
    b -= 60
if a > 23:
    a -= 24

print(a, b, c)