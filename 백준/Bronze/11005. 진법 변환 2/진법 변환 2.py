from collections import defaultdict
dic = defaultdict(str)
answer = ''
B,N = map(int,input().split())

for k in range(N):
    z = 55+k
    if k < 10:
        dic[k] = str(k)
    elif k >= 10:
        dic[k] = chr(z)
if B < N:
    answer = dic[B%N]
    print(answer)
    exit()
    
while True:
    div = B%N
    answer += str(dic[div])
    B = B // N
    if B < N:
        answer = dic[B]+answer[::-1]
        print(answer)
        break