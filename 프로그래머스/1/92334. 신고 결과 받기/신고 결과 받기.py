def solution(id_list, report, k):
    answer = []
    report_v1 = list(set(report))
    report_dict = {}
    user = {key: 0 for key in dict.fromkeys(id_list).keys()}
    for item in report_v1:
        accuser,defendant = item.split()
        if accuser in report_dict:
            report_dict[accuser].append(defendant)
        else:
            report_dict[accuser] = [defendant]
        user[defendant] += 1
    for i in id_list:
        num = 0
        if i in report_dict:
            for j in report_dict.get(i):
                if user.get(j) >= k:
                    num+=1
        answer.append(num)
    return answer