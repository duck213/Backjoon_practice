def solution(order):
    answer = 0
    a = list(map(int,str(order)))
    for i in a:
        if i!=0 and i%3==0:
            answer+=1
    return answer