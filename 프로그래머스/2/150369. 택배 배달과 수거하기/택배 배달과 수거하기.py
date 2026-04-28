def solution(cap, n, deliveries, pickups):
    answer,deli,pick = 0,0,0
    
    for i in range(n,0,-1):
        deli += deliveries[i-1]
        pick += pickups[i-1]
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += i * 2
        
    return answer