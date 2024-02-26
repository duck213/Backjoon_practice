def solution(n):
    answer = []
    string = str(n)
    for i in range(1,len(string)+1):
        answer.append(int(string[-i]))
    return answer