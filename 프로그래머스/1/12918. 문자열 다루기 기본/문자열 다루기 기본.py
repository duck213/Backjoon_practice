def solution(s):
    answer = True
    length = len(s)
    if length != 4 and length != 6:
        return False
    for i in range(length):
        if s[i].isdigit() == False:
            answer = False 
            break 
    return answer