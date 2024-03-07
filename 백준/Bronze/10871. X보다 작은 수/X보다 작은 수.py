a,b = map(int,input().split())
filt = list(map(int,input().split()))
answer = [i for i in filt if i<b]
print(*answer)