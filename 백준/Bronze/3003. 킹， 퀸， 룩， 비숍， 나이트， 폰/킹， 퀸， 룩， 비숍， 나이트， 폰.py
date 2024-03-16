answer = [1,1,2,2,2,8]
a = list(map(int,input().split()))
for i,e in zip(answer,a):
    print(i-e,end=' ')