def dfs(rank, visited, dic, a, k):
    for i in dic[a]:
        if not visited[i]:
            visited[i] = True
            rank[i][0]+=1
            dfs(rank, visited, dic, i, k)
            rank[k][1]+=1
        
def solution(n, results):
    answer = 0
    dic = {i: [] for i in range(1, n + 1)}
    rank = {i: [0,0] for i in range(1, n + 1)}
    visited = [False] * (n + 1)
    for i, j in results:
        dic[i].append(j)
    for k, v in dic.items():
        visited = [False] * (n + 1)
        if len(v) > 0:
            dfs(rank, visited, dic, k, k)

    for i,j in rank.values():
        if i+j==n-1:
            answer+=1
    return answer