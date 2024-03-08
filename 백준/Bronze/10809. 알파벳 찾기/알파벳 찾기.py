str = input()
alp = [-1]*26
for i in str:
    alp[ord(i)-97] = str.index(i)
print(*alp)