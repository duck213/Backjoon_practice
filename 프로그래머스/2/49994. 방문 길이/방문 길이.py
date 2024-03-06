def solution(dirs):
    answer = 0
    route = []
    dic = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
    x, y = 0, 0
    for i in range(len(dirs)):
        a, b = dic[dirs[i]]
        if -5 <= x+a <= 5 and -5 <= y+b <= 5:
            if [x,y,x+a,y+b] not in route and [x+a,y+b,x,y] not in route:
                route.append([x,y,x+a,y+b])
                answer+=1
            x, y = x + a, y + b
    return answer