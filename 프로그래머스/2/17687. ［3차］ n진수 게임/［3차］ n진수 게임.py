dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def solution(n, t, m, p):
    answer = ''
    string = '0'
    for i in range(t*m):
        char = ''
        while i:
            char += dic[i % n]
            i //= n
        string+= char[::-1]
    
    for i in range(p-1,len(string),m):
        answer += string[i]
        if len(answer)==t: break

    return answer