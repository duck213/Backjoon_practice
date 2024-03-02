def solution(s):
    listed = list(s)
    sort = sorted(listed, reverse=True)
    return ''.join(sort)