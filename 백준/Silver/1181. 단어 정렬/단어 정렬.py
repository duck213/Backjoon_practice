n = int(input())
name = []
for i in range(n):
    w = input()
    if w not in name:
        name.append(w)
name.sort(key=lambda x:(len(x),x))
for k in name:
    print(k)