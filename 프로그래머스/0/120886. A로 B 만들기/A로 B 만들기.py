from collections import defaultdict
def solution(before, after):
    answer = 0
    be = defaultdict(int)
    af = defaultdict(int)
    for k in range(len(before)):
        if before[k] in be:
            be[before[k]]+=1
        elif before[k] not in be:
            be[before[k]] = 0     
        if after[k] in af:
            af[after[k]]+=1
        elif after[k] not in af:
            af[after[k]] = 0
    if be==af:
        answer = 1
    else:
        answer = 0

    return answer