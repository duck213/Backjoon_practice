from itertools import permutations

def solution(numbers):
    answer = []
    listed = list(permutations(numbers,2))
    for i in range(len(listed)):
        if sum(listed[i]) not in answer:
            answer.append(sum(listed[i]))

    return sorted(answer)

