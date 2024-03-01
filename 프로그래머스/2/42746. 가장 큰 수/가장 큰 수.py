def solution(numbers):
    mapped = list(map(str, numbers))
    mapped.sort(key=lambda x : x*3 ,reverse=True)
    return str(int(''.join(mapped)))