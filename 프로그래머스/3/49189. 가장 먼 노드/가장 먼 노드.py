from collections import deque

def bfs(adj, start, visited,dic):
    queue = deque([start])
    visited[start] = True
    last = []
    max_val = 0
    cnt = 0
    while queue:
        v = queue.popleft()
        tog = False
        for i in adj[v]:
            if not visited[i]:
                queue.append(i)
                dic[i] = dic[v] + 1
                max_val = max(dic[i],max_val)
                visited[i] = True
    for i in dic.values():
        if i==max_val:
            cnt+=1
    return cnt


def solution(n, edge):
    visited = [False] * (n + 1)
    dic = {i:0 for i in range(1,n+1)}
    adj = {i:[] for i in range(n+1)}
    for a,b in edge:
        adj[a].append(b)
        adj[b].append(a)
    ans = bfs(adj, 1, visited,dic)  
    return ans