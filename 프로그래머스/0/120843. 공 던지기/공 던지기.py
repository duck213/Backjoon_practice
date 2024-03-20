def solution(numbers, k):
    answer = 0
    n = k//(len(numbers)//2)
    new = numbers * (n+1)
    start = 0
    
    for i in range(k):
        answer = new[start]
        start+=2
    return answer