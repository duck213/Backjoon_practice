# 인형 뽑기
def solution(board, moves):
    answer = 0
    bucket = []
    length = len(board)
    for m in moves:
        for catch in range(length):
            doll = board[catch][m - 1]
            if doll > 0:
                if bucket and bucket[-1] == doll:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(doll)
                board[catch][m - 1] = 0
                break
    return answer