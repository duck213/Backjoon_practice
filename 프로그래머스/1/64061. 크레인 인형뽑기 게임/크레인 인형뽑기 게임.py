def solution(board, moves):
    answer = 0
    bucket = []
    for m in moves:
        for catch in range(len(board)):
            if board[catch][m - 1] > 0:
                if len(bucket) > 0 and bucket[-1] == board[catch][m - 1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[catch][m - 1])
                board[catch][m - 1] = 0
                break
            else:
                continue
    return answer