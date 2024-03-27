def dfs(computers, v, visited):
    visited[v] = True
    for i,node in enumerate(computers[v]):
        if computers[v][i]==1 and not visited[i]:
            dfs(computers, i, visited)
            
def solution(n, computers):
    answer = 0
    visited = [False]*n
    cnt = []
    for i in range(n):
        dfs(computers,i,visited)
        if not cnt:
            cnt.append(visited.count(False))
            answer+=1
        elif cnt[-1] != visited.count(False):
            cnt.append(visited.count(False))
            answer+=1
    return answer