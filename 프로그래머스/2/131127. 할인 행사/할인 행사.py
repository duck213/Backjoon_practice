def solution(want, number, discount):
    answer = 0
    dic = {}
    
    length = len(discount)
    for w,n in zip(want, number):
        dic[w] = n
        
    for i in range(length-9):
        tens = {}
        for j in range(i, i+10):
            if discount[j] in dic:
                tens[discount[j]] = tens.get(discount[j], 0) + 1
                
        if tens == dic:
            answer += 1

    return answer