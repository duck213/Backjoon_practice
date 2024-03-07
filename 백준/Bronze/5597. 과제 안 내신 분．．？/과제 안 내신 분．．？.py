from sys import stdin
samp = [i for i in range(1,31)]
for i in range(28):
    ipt = int(stdin.readline()) # ipt = "3\n"
    samp.remove(ipt)
print(*samp)