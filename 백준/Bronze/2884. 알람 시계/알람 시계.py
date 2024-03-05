a,b = map(int,input().split())
min = b-45
if min<0: 
    a-=1
print(a%24,abs(min%60))