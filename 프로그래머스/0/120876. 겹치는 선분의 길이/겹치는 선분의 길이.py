def solution(lines):
    answer = 0
    sort_lines = sorted(lines, key=lambda x: x[0])
    max_axis = -100
    min_axis = 100
    for i,j in lines:
        max_axis = max(max_axis,j)
        min_axis = min(min_axis,i)
    store = {i:-1 for i in range(min_axis,max_axis+1)}
    for k in lines:
        i,j = k
        for z in range(i,j):
            store[z]+=1
    for a in store.values():
        if a > 0:
            answer+= 1 
    return answer