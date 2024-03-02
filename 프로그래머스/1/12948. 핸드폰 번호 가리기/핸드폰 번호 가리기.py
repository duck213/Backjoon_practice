def solution(phone_number):
    answer = ''
    # sz = size(phone_number)
    pn = len(phone_number)
    for i in range(0,pn-4):
        answer = answer + '*'
    
    return answer+phone_number[pn-4:pn]