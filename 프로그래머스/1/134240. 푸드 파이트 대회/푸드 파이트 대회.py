def solution(food):
    answer = ''
    for i, num in enumerate(food[1:]):
        temp = str(i+1)*(num//2)
        answer+=temp
    return answer + '0' + answer[::-1]


