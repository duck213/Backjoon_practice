def solution(name, yearning, photo):
    answer = []
    score = 0
    book = dict(zip(name, yearning))
    for i in range(len(photo)):
        for key, value in book.items():
            if key in photo[i]:
                score+=value
        answer.append(score)
        score = 0
    return answer