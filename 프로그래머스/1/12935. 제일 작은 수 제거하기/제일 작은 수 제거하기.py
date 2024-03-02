def solution(arr):
    answer = []
    minimum = min(arr)
    if len(arr)==1:
        answer.append(-1)
    elif len(arr) > 2:
        arr.remove(minimum)
        return arr
    return answer