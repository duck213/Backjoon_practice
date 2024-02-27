def solution(sizes):
    tmp = []
    max_x,max_y = 0,0
    for i,j in sizes:
        if i>j:
            tmp.append([j,i])
            max_x,max_y = max(j,max_x),max(i,max_y)
        else:
            tmp.append([i,j])
            max_x,max_y = max(i,max_x),max(j,max_y)

    return max_x*max_y