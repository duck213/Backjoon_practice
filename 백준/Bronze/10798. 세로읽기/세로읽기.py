max_int = 0
answer = ''
string = []
for i in range(5):
    n = input()
    max_int = max(len(n), max_int)
    string.append(n)

for a,item in enumerate(string):
    if len(item) == max_int:
        pass
    else:
        string[a] = item.ljust(max_int, '#')

for j in range(max_int):
    tmp = ''
    for i in range(5):
        if string[i][j] != '#':
            tmp += string[i][j]
    answer+=tmp
print(answer)