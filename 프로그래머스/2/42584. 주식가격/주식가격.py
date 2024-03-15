def solution(prices):
    answer = []
    cnt = 0
    length = len(prices)
    for n in range(length):
        cnt=0
        for j in range(n+1,length):
            if prices[n]>prices[j]:
                cnt+=1
                break
            cnt+=1
        answer.append(cnt)
    return answer

