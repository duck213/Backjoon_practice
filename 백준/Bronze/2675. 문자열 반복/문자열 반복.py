n = int(input())
list = [[k for k in input().split()] for i in range(n)]
for a in list:
    char = []
    for i in range(len(a[1])):
        char.append(a[1][i] * int(a[0]))
    print(''.join(char))