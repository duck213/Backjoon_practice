from collections import deque
def solution(n, lost, reserve):
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    #print(answer,lost,reserve)
    lost_q = deque(lost)
    reserve_q = deque(reserve)
    count = 1
    while len(reserve_q) > 0 and len(lost_q) > 0:
        buffer = len(lost_q)
        if abs(reserve_q[0] - lost_q[0]) == 1:
            lost_q.popleft()
            reserve_q.popleft()
            answer+=1
            count = 1
        elif count==buffer or buffer == 0:
            reserve_q.popleft()
            count = 1
        else:
            count += 1
            lost_q.rotate(-1)
        if buffer == 0 or len(lost_q) == 0 or len(reserve_q) == 0:
            break
    return answer