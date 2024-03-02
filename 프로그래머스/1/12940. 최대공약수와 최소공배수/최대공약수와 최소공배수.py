def solution(n, m):
    GCD = 0
    LCM = 0
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0:
            GCD = i
            break
    for j in range(max(n,m),(n*m)+1):
        if j%n==0 and j%m==0:
            LCM = j
            break
    return [GCD,LCM]