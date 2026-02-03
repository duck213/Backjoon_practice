def solution(mats, park):
    answer = 0
    width,height = len(park[0]),len(park)
    mats.sort(reverse=True)
    for m in mats:
        for row in range(height):
            for col in range(width):
                if row + m > height or col + m > width:
                    continue
                avail = True
                for i in range(row, row + m):
                    for j in range(col, col + m):
                        if park[i][j] != "-1":  
                            avail = False
                if avail:
                    return m
    return -1