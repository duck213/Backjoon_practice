n = int(input())
lst = [[k for k in input().split()] for i in range(n)]
for item in lst:
    num = float(item[0])
    for i in item:
        if i=='@':
            num *= 3
        elif i=='%':
            num += 5
        elif i=='#':
            num -= 7
    print("{0:.2f}".format(num))