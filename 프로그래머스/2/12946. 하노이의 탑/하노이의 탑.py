def solution(n):
    answer = []

    def hanoi(n, start, to, via):
        if n == 1:
            answer.append([start, to])
        else:
            hanoi(n - 1, start, via, to)
            answer.append([start, to])
            hanoi(n - 1, via, to, start)
        return answer

    result = hanoi(n, 1, 3, 2)
    return result


