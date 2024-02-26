import math
def solution(n):
    res = [True for i in range(n+1)] 
    for i in range(2,int(math.sqrt(n))+1):
        if res[i]:
            j=2 
            while i*j<=n:
                res[i*j] = False
                j+=1
    return res[2:].count(True)

