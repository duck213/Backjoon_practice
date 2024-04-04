def solution(n, times):
    start,end = 1,times[-1]*n
    while start<=end:
        peop = 0
        mid = (start+end)//2
        for i in times:
            peop += mid//i
            if peop>=n: break
        
        if peop>=n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer