def solution(a, b):
    combined = int(str(a)+str(b))
    if combined >= 2 * a * b:
        answer = combined
    else:
        answer = 2 * a * b
    return answer