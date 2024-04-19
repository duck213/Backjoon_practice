import math
def solution(fees, records):
    answer = []
    park = {}
    a,b,c,d = fees
    for rec in records:
        time,num,ac = rec.split()
        if ac=='IN' and num not in park:
            park[num] = [time,0,ac,0]
        elif ac=='IN' and num in park:
            park[num][0] = time
            park[num][2] = ac
        elif ac=='OUT':
            hour1, min1 = park[num][0].split(":")
            hour2, min2 = time.split(":")
            mini = 60*(int(hour2)-int(hour1)) + int(min2)-int(min1)
            park[num][0] = time
            park[num][1] += mini
            park[num][2] = ac
            #print(park,num,mini)
    for k,v in park.items():
        q,w,e,n = v
        if e=='IN':
            hour1, min1 = park[k][0].split(":")
            hour2, min2 = 23,59
            mini = 60*(hour2-int(hour1)) + abs(min2-int(min1))
            park[k][1] += mini
            park[k][2] = "OUT"
        if park[k][1] <= a:
            park[k][3] = b
        else:
            park[k][3] = b + math.ceil((park[k][1]-a)/c) * d
    answer = sorted(park.items(), key=lambda x:x[0])
    answer = [x[3] for z,x in answer]
    return answer