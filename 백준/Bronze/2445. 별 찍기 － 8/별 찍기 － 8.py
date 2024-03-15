a = int(input())
str = '*'
for i in range(1, a+1):
    print(str * i + ' ' * 2*(a-i) + str * i)
for i in range(a-1, 0, -1):
    print(str * i + ' ' * 2*(a-i) + str * i)