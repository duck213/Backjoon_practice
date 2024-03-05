def end(cnt,n):
    host,order = (cnt-1)//n, (cnt-1)%n
    return [order+1,host+1]
    
def solution(n, words):
    answer = []
    basket = []
    before = ""
    cnt = 1
    for item in words:
        if item not in basket:
            basket.append(item)
        elif item in basket:
            answer = end(cnt,n)
            break

        if cnt > 1 and before!=item[0]:
            answer = end(cnt,n)
            break
        before = item[-1]     
        cnt+=1
    return [0,0] if not answer else answer