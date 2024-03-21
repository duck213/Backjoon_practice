from collections import deque
def solution(s):
    answer = 0
    length = len(s)
    match = {'{': '}', '[': ']', '(': ')'}
    tmp = deque()
    comp = deque()
    for i in range(length):
        if s[0] in [']', '}', ')']:
            s = s[1:] + s[0]
            continue
        Fake = False
        for j in s:
            if j in ['{', '[', '(']:
                tmp.append(j)
                comp.appendleft(match[j])
            elif tmp and j == match[tmp[-1]]:
                tmp.pop()
                comp.popleft()
            else:
                Fake = True
                break

        answer += 1 if not tmp and Fake == False else 0
        s = s[1:] + s[0]
    return answer