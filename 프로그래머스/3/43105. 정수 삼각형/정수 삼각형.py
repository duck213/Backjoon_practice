def solution(triangle):
    length = len(triangle)
    if length == 1:
        return triangle[0][0]
    for i in triangle:
        i.insert(0,0)
        i.append(0)
    for i in range(1, length):
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] = max(triangle[i][j]+triangle[i-1][j-1], triangle[i][j]+triangle[i - 1][j])
    return max(triangle[-1])