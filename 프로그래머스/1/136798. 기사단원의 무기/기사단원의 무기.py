import math
def solution(number, limit, power):
    count = 0
    factors = [1]
    for i in range(2,number+1):
        for j in range(1,int(math.sqrt(i))+1):
            if i % j == 0:
                count+=2
            if i / j == j:
                count-=1        
        count = power if count > limit else count
        factors.append(count)
        count = 0
    return sum(factors)

