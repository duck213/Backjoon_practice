import math

def solution(progresses, speeds):
    answer = []
    rest = []
    count = 0

    for pro, sp in zip(progresses, speeds):
        rest.append(math.ceil((100 - pro) / sp))
    
    last = rest[0]
    
    for i in range(len(rest)):
        if rest[i] <= last:
            count+=1
        else:
            answer.append(count)
            count = 1
            last = rest[i]
        
    answer.append(count)
    return answer