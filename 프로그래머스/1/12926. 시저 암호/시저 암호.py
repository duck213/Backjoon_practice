def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if 64 < ord(s[i]) < 91:
            answer += chr(ord("A") + (ord(s[i]) + n - ord("A")) % 26)
        elif 96 < ord(s[i]) < 123:
            answer += chr(ord("a") + (ord(s[i]) + n - ord("a")) % 26)
        else:
            answer += " "
    return answer