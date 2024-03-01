def solution(a, b, n):
    # 빈병 a 를 가져다주면 b 를 준다.
    spare = 0
    while n >= a:
        spare += (n//a) * b
        n = n%a + (n//a) * b
    return spare