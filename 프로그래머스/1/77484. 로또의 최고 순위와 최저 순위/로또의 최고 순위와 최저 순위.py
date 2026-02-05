from collections import defaultdict
def solution(lottos, win_nums):
    answer = [6,6]
    cnt = 0
    dic = defaultdict(int)
    #dic[0] = -1
    for i in lottos:
        dic[i] += 1
    for k,v in dic.items():
        if k in win_nums:
            cnt+=1
            if cnt>1:
                answer[0] -= 1
                answer[1] -= 1
    if dic[0] > 0:
        answer[0] -= dic[0]
    if answer[0] == 0:
        answer[0] += 1
    return answer