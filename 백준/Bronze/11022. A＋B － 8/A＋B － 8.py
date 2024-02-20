n = int(input())
list = [[int(k) for k in input().split()] for i in range(n)]
for j in range(0,n):
    print('Case #'+str(j+1)+': '+str(list[j][0])+' + '+str(list[j][1])+' = '+str(sum(list[j])))