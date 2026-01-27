from collections import deque
def valid_move(ny,nx,n,m,maps):
    return 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X'

def bfs(maps, n,m):
    q = deque()

    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    w, z = 0, 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                visited[i][j][0] = True
                q.append((i,j,0,0))
            elif maps[i][j] == "E":
                z, w = i, j
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while q:
        y,x,key,dist = q.popleft()
        if y==z and x==w and key == 1:
            return dist
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if not valid_move(ny,nx,n,m,maps):
                continue

            if maps[ny][nx] == "L":
                if not visited[ny][nx][key]:
                    visited[ny][nx][1] = True
                    q.append((ny,nx,1,dist+1))
            else:
                if not visited[ny][nx][key]:
                    visited[ny][nx][key] = True
                    q.append((ny,nx,key,dist+1))

    return -1


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    return bfs(maps, n, m)