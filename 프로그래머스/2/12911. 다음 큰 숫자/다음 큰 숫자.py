def solution(n):
    cnt = bin(n).count("1")
    n+=1
    while bin(n).count("1")!=cnt: 
        n+=1
    return n