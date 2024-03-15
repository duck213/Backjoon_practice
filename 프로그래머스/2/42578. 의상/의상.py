def solution(clothes):
    answer = 1
    fashion = dict()
    for cloth,kind in clothes:
        if kind not in fashion:
            fashion[kind] = [cloth]
        elif kind in fashion:
            fashion[kind].append(cloth)
    for key,value in fashion.items():
        answer*=(len(value)+1)
    return answer-1