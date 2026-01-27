def getAns(n, y, width, diagonal1, diagonal2):
    answer = 0
    if n == y:
        answer+=1
    else:
        for i in range(n):
            if width[i] or diagonal1[i+y] or diagonal2[i-y+n]:
                continue
            width[i] = diagonal1[i+y] = diagonal2[i-y+n] = True # add queen

            answer += getAns(n, y+1, width, diagonal1, diagonal2) # recursive

            width[i] = diagonal1[i+y] = diagonal2[i-y+n] = False # remove queen

    return answer

def solution(n):
    answer = getAns(n, 0, [False] * n, [False] * (n*2), [False] * (n*2))
    return answer