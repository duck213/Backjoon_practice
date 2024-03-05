a,b,c = map(int, input().split())
if a==b==c: 
    print(10000+a*1000)
elif a==b and b!=c: 
    print(1000+a*100)
elif a!=b and b==c: 
    print(1000+b*100)
elif a==c and c!=b: 
    print(1000+c*100)
elif a!=b!=c: 
    kas = [a,b,c]
    print(max(kas)*100)