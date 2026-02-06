
def solution(board):
    width = len(board[0])
    depth = len(board)
    for i in range(1,depth):
        for j in range(1,width):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1])+1
    answer = max(max(i) for i in board)     
    return answer**2
