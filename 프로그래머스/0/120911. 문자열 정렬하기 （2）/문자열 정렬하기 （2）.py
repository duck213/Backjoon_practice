def solution(my_string):
    answer = ''
    char = list(my_string.lower())
    char.sort()
    return ''.join(char)