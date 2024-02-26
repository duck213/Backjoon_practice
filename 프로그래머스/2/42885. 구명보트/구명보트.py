from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    deq = deque(people)
    while deq:
        if len(deq)>1:
            left = deq.popleft()
            right = deq.pop()
            side = left + right
            if side>limit:
                deq.appendleft(left)
        elif len(deq) == 1:
            deq.pop()
        answer+=1
    return answer