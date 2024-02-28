from collections import Counter
def solution(k, tangerine):
    answer,count = 0,0
    temp = Counter(tangerine)
    temp = temp.most_common()
    for i,j in temp:
        count+=j
        answer+=1
        if count>=k:
            break
    return answer