total = int(input())
process = 0
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    process += a*b
if process==total:
    print("Yes")
else:
    print("No")