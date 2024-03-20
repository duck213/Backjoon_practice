import heapq as hq
def solution(jobs):
    answer = 0
    hq.heapify(jobs)
    length = len(jobs)
    start = -1
    cnt, now, num = 0, 0, 0
    working = []
    while cnt < length:
        for q,w in jobs:
            if start < q <= now:
                hq.heappush(working,[w, q])

        if len(working)>0:
            a = hq.heappop(working)
            start = now
            now += a[0]
            answer += now - a[1]
            cnt+=1
        else:
            now+=1
    return answer // length