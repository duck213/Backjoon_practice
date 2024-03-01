import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while len(scoville) > 1:
        pop1 = hq.heappop(scoville)
        if pop1 >= K:
            return answer
        else:  
            pop2 = hq.heappop(scoville)
            hq.heappush(scoville, pop1 + pop2 * 2)
            answer += 1
    if scoville[0] >= K:
        return answer
    return -1