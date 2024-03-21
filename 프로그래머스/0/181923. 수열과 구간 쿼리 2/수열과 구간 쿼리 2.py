def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        result = []
        for i in arr[s:e+1]:
            if i>k:
                result.append(i)
        if not result:
            answer.append(-1)
        else:
            answer.append(min(result))
    return answer