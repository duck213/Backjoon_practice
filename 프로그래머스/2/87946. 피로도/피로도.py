from itertools import permutations as pm
import numpy as np
def solution(k, dungeons):
    row = len(np.array(dungeons))
    List = list(pm(dungeons,row))
    stage = []
    for item in list(List):
        rest = k
        answer = 0
        for health,consume in item:
            #print('before:',rest,consume)
            if rest>=health:
                rest = rest - consume
                answer += 1
                if answer not in stage:
                    stage.append(answer)
                if answer == row:
                    return answer
            elif rest < health:
                continue
    return max(stage)