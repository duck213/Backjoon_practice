from collections import defaultdict
dic = defaultdict(int)
answer = 0
B,N = input().split()
length = len(B)-1
N = int(N)

if N > 10:
    for k in range(N-10):
        z = 65+k
        dic[chr(z)] = 10+k

for i,b in enumerate(B):
    if 48 <= ord(b) <= 57:
        answer += int(b) * (N ** (length - i))
    else:
        answer+=dic[b]*(N**(length-i))
print(answer)