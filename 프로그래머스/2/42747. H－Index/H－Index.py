def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i, index in enumerate(citations,1):
        if i<=index:
            answer = i
    return answer