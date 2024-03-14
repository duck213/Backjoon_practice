a = int(input())
str = '*'
for i in range(a, 0, -1):
    print(' ' * (a-i) + str * i)