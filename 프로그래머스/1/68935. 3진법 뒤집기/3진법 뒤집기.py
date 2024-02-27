def solution(n):
    reverse = ''
    while n > 0:
        n,div = divmod(n,3)
        reverse += str(div)
    return int(reverse,3)