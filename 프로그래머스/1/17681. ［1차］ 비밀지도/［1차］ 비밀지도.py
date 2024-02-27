def solution(n, arr1, arr2):
    answer = []
    string = ''
    for i in range(n):
        result = str(bin(arr1[i] | arr2[i]))[2:].zfill(n)
        string = ''
        for j in range(0, len(result)):
            if result[j]=='1':
                string+='#'
            elif result[j] == '0':
                string+=' '

        answer.append(string)
    return answer