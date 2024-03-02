def solution(s):
    answer = ''
    length = len(s)
    answer = s[length//2] if length % 2 == 1 else s[length//2-1:length//2+1]
    return answer