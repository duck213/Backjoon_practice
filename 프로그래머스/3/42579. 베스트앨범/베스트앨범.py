def solution(genres, plays):
    answer = []
    count = {}
    music = {}
    for i,(gen,pl) in enumerate(zip(genres,plays)):
        if gen not in count:
            count[gen] = pl
            music[gen] = [(pl,i)]
        else:
            count[gen] += pl
            music[gen].append((pl,i))     
        music[gen].sort(key = lambda x: (x[0],-x[1]), reverse=True)

    rank = list(map(lambda x: x[0], sorted(count.items(), key=lambda x:x[1],reverse=True)))
    for i in rank:
        cnt = 0
        for pla,k in music[i]:
            answer.append(k)
            cnt+=1
            if cnt==2: break
        
    return answer
