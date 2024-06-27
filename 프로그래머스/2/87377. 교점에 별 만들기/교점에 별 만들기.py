def solution(line):
    intersect = []
    n = len(line)
    max_x = max_y = -100000000000
    min_x = min_y = 100000000000
    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n):
            c, d, f = line[j]
            if (a * d) - (b * c) == 0: continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if x.is_integer() and y.is_integer():
                x, y = int(x), int(y)
                intersect.append([x, y])
                max_x, max_y = max(x, max_x), max(y, max_y)
                min_x, min_y = min(x, min_x), min(y, min_y)

    width = abs(max_x - min_x) + 1
    height = abs(max_y - min_y) + 1
    answer = [['.'] * width for _ in range(height)]
    intersect = sorted(intersect, key=lambda i: -i[1])
    for dx, dy in intersect:
        ny = max_y - dy
        nx = dx - min_x
        answer[ny][nx] = '*'
    return list(map(''.join, answer))