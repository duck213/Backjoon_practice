def solution(progresses, speeds):
    answer = []
    count = 0
    point = 0
    length = len(speeds)
    while progresses[-1] <= 100:
        progresses = [x+y if x+y<101 else 100 for x,y in zip(progresses, speeds)]
        if progresses[point]==100:
            for i in range(point,length):
                if progresses[i]==100:
                    count+=1
                else:
                    break
            answer.append(count)
            if sum(progresses) == 100*length:
                return answer
            if length-1 > point:
                point+=count
            else:
                pass
            count = 0