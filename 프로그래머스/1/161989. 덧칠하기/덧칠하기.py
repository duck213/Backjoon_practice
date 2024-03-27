def solution(n, m, section):
    answer = 1
    start = section[0]
    end = section[0]+m-1
    for i in section:
        if start<=i<=end:
            pass
        else:
            start=i
            end=i+m-1
            answer+=1
    
    return answer