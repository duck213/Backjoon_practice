def solution(rny_string):
    answer = ''
    listed = list(rny_string)
    for i in range(len(listed)):
        if listed[i] == 'm':
            listed[i] = "rn"
    return "".join(listed)