def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[0])
    point = routes[0][1]
    for a,b in routes:
        if b<=point:
            point = b
        elif a<=point<b:
            pass
        elif point<a<=b:
            point = b
            answer+=1
    return answer