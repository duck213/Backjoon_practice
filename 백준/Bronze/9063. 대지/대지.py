n = int(input())
a_x,b_y=[],[]
for i in range(n):
    a,b = map(int,input().split())
    a_x.append(a)
    b_y.append(b)
square = (max(a_x)-min(a_x))*(max(b_y)-min(b_y))
print(square)