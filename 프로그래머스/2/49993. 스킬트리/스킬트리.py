from collections import deque


def solution(skill, skill_trees):
    answer = 0
    ency = deque(skill)
    for item in skill_trees:
        temp = deque(item)
        idx = 0
        tog = True
        for i in temp:
            if i in ency and ency.index(i) > ency.index(skill[idx]):
                tog = False
                break
            elif i in ency and ency.index(i) == ency.index(skill[idx]):
                idx += 1
            elif i not in ency:
                pass
        if tog:
            answer += 1
    return answer