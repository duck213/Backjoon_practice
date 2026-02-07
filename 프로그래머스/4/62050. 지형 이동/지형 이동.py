from heapq import heappop, heappush

def solution(land, height):
    answer = 0
    length = len(land)
    
    dy = [-1,0,1,0]
    dx = [0,1,0,-1]
    visited = [[False]*length for _ in range(length)]
    hq = []
    heappush(hq, [0,0,0])
    
    while hq:
        cost, i, j = heappop(hq)
        if not visited[i][j]:
            visited[i][j] = True
            answer+=cost
            for z in range(4):
                y,x = i+dy[z], j+dx[z]
                if 0 <= y < length and 0 <= x < length:
                    stand = abs(land[y][x]-land[i][j]) 
                    if stand > height:
                        gap = stand
                    else:
                        gap = 0
                
                    heappush(hq, [gap,y,x])
                    
    return answer