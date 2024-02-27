
def solution(N, stages):
    user = len(stages)
    stage = dict()
    for i in range(1,N+1):
        
        if user!=0:
            fail = stages.count(i)
            stage[i] = fail/user
            user -= fail
        else:
            stage[i]=0
        
    answer = sorted(stage, key=lambda x: stage[x], reverse=True)
    return answer