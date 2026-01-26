def solution(enroll, referral, seller, amount):
    answer = []
    group = dict(zip(enroll, referral))
    interest = {name: 0 for name in enroll}

    for i in range(len(seller)):
        step = seller[i]
        money = amount[i] * 100
        while money > 0 and step != '-':
            interest[step] +=  money - money // 10
            step = group[step]
            money //= 10

    for mem, val in interest.items():
        answer.append(val)
    return answer