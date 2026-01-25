def solution(record):
    answer = []
    dic = {}
    for w in record:
        res = w.split(" ")
        if res[0] != 'Leave':
            dic[res[1]] = res[2]
    
    for chat in record:
        res = chat.split(" ")
        if res[0] == 'Enter':
            answer.append(dic[res[1]]+"님이 들어왔습니다.")
        elif res[0] == 'Leave':
            answer.append(dic[res[1]]+"님이 나갔습니다.")
            
    return answer