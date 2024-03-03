def solution(t, p):
    answer = 0
    length = len(p)
    str_range = len(t) - length + 1
    for i in range(str_range):
        if int(t[i:i+length]) <= int(p):
            answer+=1
    return answer