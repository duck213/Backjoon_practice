def solution(s):
    answer = 0
    listed = list(s)
    if listed[0]=='+':
        answer = int("".join(listed[1:]))
    elif listed[0]=='-':
        answer = -int("".join(listed[1:]))
    else:
        answer = int("".join(listed[:]))
    return answer