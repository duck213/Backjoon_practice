def solution(s):
    answer = [-1]
    count = 0
    for i in range(1,len(s)):
        for j in range(i,0,-1):
            count+=1
            if s[i] == s[j-1]:
                answer.append(count)
                break
            elif s[i] != s[j-1] and j==1:
                answer.append(-1)
            else:
                pass
        count=0
    return answer