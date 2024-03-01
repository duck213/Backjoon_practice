from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'
    deq1 = deque(cards1)
    deq2 = deque(cards2)
    length = len(goal)
    for i in range(length):
        if len(deq1) > 0 and goal[i]==deq1[0]:
            deq1.popleft()
        elif len(deq2) > 0 and goal[i]==deq2[0]:
            deq2.popleft()
        else:
            answer = 'No'
            break
    return answer