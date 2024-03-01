def solution(strings, n):
    return sorted(strings, key = lambda x: (ord(x[n]), x[:n+1],x[n:]))