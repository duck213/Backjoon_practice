def solution(n):
    ans = 1
    if n<=2: return ans
    while n!=2:
        if n%2==1:
            n-=1
            ans+=1
        elif n%2==0:
            n/=2
    return ans