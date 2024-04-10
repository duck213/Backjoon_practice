import re
def solution(dartResult):
    store = []
    tmp_char = ''
    dic = {'S':1,'D':2,'T':3}
    length = len(dartResult)
    for i in range(length):
        if dartResult[i].isdigit():
            tmp_char+=dartResult[i]
        elif dartResult[i].isalpha():
            store.append(int(tmp_char)**dic[dartResult[i]])
            tmp_char = ''
        elif dartResult[i]=='*':
            if len(store)==1:
                store[-1]*=2
            elif len(store)>1:
                store[-1]*=2
                store[-2]*=2
        elif dartResult[i]=='#':
            store[-1] = -store[-1]
    return sum(store)