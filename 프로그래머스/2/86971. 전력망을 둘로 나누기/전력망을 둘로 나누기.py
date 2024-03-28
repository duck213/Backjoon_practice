from collections import deque

def bfs(graph, start, visited, linked):
    q = deque([start])
    visited[start] = True
    cnt = 1
    while q:
        v = q.popleft()
        for i in graph[v]:  
            if not visited[i] and linked[v][i]:
                q.append(i)
                cnt += 1
                visited[i] = True
    return cnt

def solution(n, wires):
    answer = 100

    edge = [[] for k in range(n + 1)]
    for i, j in wires:
        edge[i].append(j)
        edge[j].append(i)
    linked = [[True] * (n + 1) for z in range(n + 1)]

    for i, j in wires:
        visited = [False] * (n + 1)
        linked[i][j] = False
        a = bfs(edge, i, visited, linked)
        b = bfs(edge, j, visited, linked)
        linked[i][j] = True
        answer = min(answer, abs(a - b))
    return answer