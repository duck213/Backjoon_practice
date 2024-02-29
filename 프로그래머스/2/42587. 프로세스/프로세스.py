from collections import deque
def solution(priorities, location):
    answer = 1
    prior = deque(priorities)
    loc = deque([i for i in range(len(prior))])
    while len(prior) > 0:
        if prior[0] == max(prior):
            if loc[0] == location:
                break
            answer+=1
            prior.popleft()
            loc.popleft()  
        elif prior[0] != max(prior):
            prior.rotate(-1)
            loc.rotate(-1)
    return answer