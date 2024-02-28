def solution(s):
    answer = True
    queue = []
    for i in range(len(s)):
        queue.append(s[i])
        if len(queue) > 1 and queue[-2:] == ['(',')']:
            queue.pop()
            queue.pop()
    if queue == []:
        answer = True
    else:
        answer = False

    return answer