a = int(input())
str = '*'
for i in range(1, a+1):
    print(' ' * (a-i) + str * (2*i-1))
for i in range(a-1, 0, -1):
    print(' ' * (a-i) + str * (2*i-1))