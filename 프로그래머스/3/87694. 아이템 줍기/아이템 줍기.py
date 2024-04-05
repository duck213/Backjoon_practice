from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
limit = 101

def bfs(graph, characterX, characterY, itemX, itemY):
    queue = deque()
    queue.append((characterX*2, characterY*2))
    cnt = 1
    ans = []
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= limit or ny < 0 or ny >= limit:
                continue
            if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                continue
            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            if nx == itemX*2 and ny == itemY*2:
                ans.append(cnt)
                return ans

def solution(rectangle, characterX, characterY, itemX, itemY):
    coordinate = []
    for i in range(limit):
        tmp = []
        for j in range(limit):
            tmp.append(0)
        coordinate.append(tmp)
    for rec in rectangle:
        s_x, s_y, t_x, t_y = [i*2 for i in rec]
        for i in range(t_x - s_x + 1):
            if coordinate[s_x + i][s_y] != 2:
                coordinate[s_x + i][s_y] = 1
            if coordinate[s_x + i][t_y] != 2:
                coordinate[s_x + i][t_y] = 1

        for j in range(1, t_y - s_y):
            if coordinate[s_x][s_y + j] != 2:
                coordinate[s_x][s_y + j] = 1
            if coordinate[t_x][s_y + j] != 2:
                coordinate[t_x][s_y + j] = 1

        for i in range(s_x + 1, t_x):
            for j in range(s_y + 1, t_y):
                coordinate[i][j] = 2
    answer = bfs(coordinate, characterX, characterY, itemX, itemY)
    return min(answer)//4