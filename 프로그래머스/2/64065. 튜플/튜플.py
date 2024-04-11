def solution(s):
    dic = {}
    char = ''
    length = len(s)
    for i in range(1,length):
        if s[i]=="{":
            pass
        elif s[i]=="}" or s[i]==",":
            if len(char) > 0:
                if char not in dic:
                    dic[char] = 1
                elif char in dic:
                    dic[char] += 1
                char = ''
            else:
                continue
        elif s[i].isdigit():
            char+=s[i]
    arr = sorted(dic.items(), key=lambda x: x[1],reverse=True)
    answer = [int(i[0]) for i in arr]
    return answer