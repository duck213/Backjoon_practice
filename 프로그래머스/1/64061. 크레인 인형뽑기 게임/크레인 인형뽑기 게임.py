def solution(board, moves):
    answer = 0
    length = len(board)
    bucket = []
    point = None
    for m in moves:
        for catch in range(length):
            if board[catch][m - 1] > 0:
                if point == board[catch][m - 1]:
                    answer += 2
                    del bucket[-1]
                    if bucket is []:
                        point = None
                    elif len(bucket) > 0:
                        point = bucket[-1]
                    board[catch][m - 1] = 0
                    break
                bucket.append(board[catch][m - 1])
                point = board[catch][m - 1]
                board[catch][m - 1] = 0
                break
            else:
                continue
    return answer