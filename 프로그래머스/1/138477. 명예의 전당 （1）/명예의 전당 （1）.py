def solution(k, score):
    answer = []
    score_list = []
    for i in range(len(score)):
        score_list.append(score[i])
        score_list.sort()
        answer.append(min(score_list[-k:]))
    return answer