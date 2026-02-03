from collections import deque
def solution(targets):
    answer,loc = 0,0
    targets.sort(key=lambda x:x[1])
    for i in range(len(targets)):
        if targets[i][0] < loc:
            continue
        else:
            loc = targets[i][1]
            answer+=1

    return answer