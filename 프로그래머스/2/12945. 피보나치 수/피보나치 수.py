def solution(n):
    a0,a1 = 0,1
    for i in range(2,n+1):
        a2 = a0 + a1
        a0,a1 = a1,a2
    answer = a2 % 1234567
    return answer