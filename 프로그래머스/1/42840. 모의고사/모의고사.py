def solution(answers):
    conclude = []
    spj_1 = [1,2,3,4,5]
    spj_2 = [2,1,2,3,2,4,2,5]
    spj_3 = [3,3,1,1,2,2,4,4,5,5]
    counts = [0,0,0]
    for i, answer in enumerate(answers):
        a,b,c = i%5,i%8,i%10
        if answer==spj_1[a]:
            counts[0]+=1
        if answer==spj_2[b]:
            counts[1]+=1
        if answer==spj_3[c]:
            counts[2]+=1

    for j, point in enumerate(counts):
        if point == max(counts):
            conclude.append(j+1)
    return conclude