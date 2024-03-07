init = [list(map(int,input().split())) for _ in range(9)]
ma,x,y = 0,0,0
for i in range(9):
    for j in range(9):
        if ma <= init[i][j]:
            x,y = i,j
            ma = init[i][j]
print(ma)
print(x+1,y+1)