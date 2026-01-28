from collections import Counter
def solution(topping):
    answer = 0
    cnt = Counter(topping)
    bro = set()
    for t in topping:
        bro.add(t)
        cnt[t] -= 1
        if cnt[t] == 0:
            cnt.pop(t)
        if len(cnt)==len(bro):
            answer+=1
    return answer