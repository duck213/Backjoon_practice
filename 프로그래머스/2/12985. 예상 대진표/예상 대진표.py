import math
def solution(n,a,b):
    answer = 1
    route = n//2
    if a>b:
        a,b=b,a
    diff = b - a
    exp = int(math.log2(n))
    if b-a==1 and b%2==0:
        return answer
    else:
        for i in range(exp):
            if a <= route < b:
                answer = exp - i
                break
            elif a > route and b > route:
                a = a - route
                b = b - route
            route = route // 2
    return answer