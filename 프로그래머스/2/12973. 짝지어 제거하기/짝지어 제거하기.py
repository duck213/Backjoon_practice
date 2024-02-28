from collections import deque
def solution(s):
    answer = 0
    queue = deque(s)
    store = deque()
    while len(queue) > 0:
        if len(queue) == 1 or queue[0] != queue[1]:
            k = queue.popleft()
            store.append(k)
        elif queue[0] == queue[1]:
            queue.popleft()
            queue.popleft()
        if len(store) > 1 and store[-1] == store[-2]:
            store.pop()
            store.pop()
    if len(queue) == 0 and len(store) == 0:
        answer = 1
    return answer