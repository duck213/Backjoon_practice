def solution(arr):
    answer = []
    past = -1
    for i in range(len(arr)):
        present = arr[i]
        if present != past:
            answer.append(present)
        past = present
    return answer