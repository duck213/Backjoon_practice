from functools import reduce
def solution(data, col, row_begin, row_end):
    data.sort(reverse=True)
    data.sort(key=lambda x: x[col-1])
    h = []
    for i in range(row_begin,row_end+1):
        k = 0
        for j in data[i-1]:
            k += j % i
        h.append(k)
    k = reduce(lambda x,y:x^y,h)
    return k