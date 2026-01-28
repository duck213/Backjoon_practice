def solution(n, stations, w):
    answer = 0
    location = 1
    i = 0
    while location <= n:
        if i < len(stations) and location >= (stations[i] - w): 
            location = stations[i] + w + 1
            i+=1
        else:
            location += 2 * w + 1
            answer+=1
        
    return answer