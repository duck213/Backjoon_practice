def solution(a, d, included):
    answer = a if included[0]==True else 0
    for i in range(1,len(included)):
        a += d
        if included[i]==True:
            answer+=a
    return answer

