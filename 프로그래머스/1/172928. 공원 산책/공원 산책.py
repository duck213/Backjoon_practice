def solution(park, routes):
    answer = []
    height,width = len(park), len(park[0])

    direct = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    for row in range(height):
        for col in range(width):
            if park[row][col]=='S':
                answer = [row, col]
                break
    for line in routes:
        move, cnt = line.split(" ")
        cnt = int(cnt)
        dr, dc = direct[move]
        new_row, new_col = answer[0], answer[1]
        can_move = True
        for i in range(cnt):
            new_row += dr
            new_col += dc
            if not (0 <= new_row < height and 0 <= new_col < width):
                can_move = False
                break
            if park[new_row][new_col]=='X':
                can_move = False
                break
        if can_move: 
            answer = [new_row, new_col]
    return answer