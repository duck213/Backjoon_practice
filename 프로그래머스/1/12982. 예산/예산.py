def solution(d, budget):
    count = 0
    #price = budget
    sort_list = sorted(d)
    for i in sort_list:
        if budget < i:
            break
        budget-=i
        count+=1
    return count