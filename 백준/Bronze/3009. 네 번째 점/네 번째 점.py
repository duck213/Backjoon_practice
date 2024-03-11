a_x,b_y = [],[]
for i in range(3):
    a,b = map(int,input().split())
    a_x.append(a)
    b_y.append(b)
x,y = a_x[0] ^ a_x[1] ^ a_x[2], b_y[0] ^ b_y[1] ^ b_y[2]
print(x,y)