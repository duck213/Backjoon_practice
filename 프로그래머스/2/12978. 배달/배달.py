import heapq as hq
from collections import defaultdict
INF = 500000

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N+1)]
    for start,end,cost in road:
        graph[start].append((end,cost))
        graph[end].append((start,cost))
        
    time = [INF]*(N+1)
    time[1] = 0
    q = []
    hq.heappush(q, (0,1)) # cost, node
    while q:
        cost, node = hq.heappop(q)

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < time[neighbor]:
                time[neighbor] = new_cost
                hq.heappush(q,(new_cost, neighbor))
        
    for i in time:
        if i <=K:
            answer+=1

    return answer