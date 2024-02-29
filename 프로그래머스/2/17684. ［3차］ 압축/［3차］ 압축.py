from collections import deque
def solution(msg):
    answer = []
    index = 0
    w = ''
    ency = {}
    for i in range(65, 91):
        index += 1
        ency[chr(i)] = index
    q = deque(msg)
    while q:
        w += q.popleft()
        if not q:
            answer.append(ency[w])
            break
        if w + q[0] not in ency:
            answer.append(ency[w])
            index += 1
            ency[w + q[0]] = index
            w = ''
    return answer