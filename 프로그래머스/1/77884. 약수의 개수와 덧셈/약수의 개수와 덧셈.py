import math
def solution(left, right):
    answer = 0
    count = 0
    for param in range(left,right+1):
        for i in range(1, int(math.sqrt(param))+1):
            if param % i == 0:
                count+=2
            if param / i == i:
                count-=1
        answer += param if count % 2 == 0 else -param
        count = 0
    return answer