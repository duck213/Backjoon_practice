def solution(my_string):
    answer = [0]*52
    for i in list(my_string):
        if 64<ord(i)<91:
            answer[ord(i)-65]+= 1
        elif 96<ord(i)<123:
            answer[ord(i)-71]+= 1
    return answer