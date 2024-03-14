a = int(input())
str = '*'
for i in range(a, 0, -1):
    print(' ' * (i-1) + str.rstrip())
    str = str + '*'