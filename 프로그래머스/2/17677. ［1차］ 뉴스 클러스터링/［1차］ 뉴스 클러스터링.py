def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    str1_len, str2_len = len(str1), len(str2)
    str1_store, str2_store = [], []
    for e in range(max(str1_len,str2_len)):
        if e+1<str1_len and str1[e:e+2].isalpha():
            str1_store.append(str1[e:e+2])
        if e+1<str2_len and str2[e:e+2].isalpha():
            str2_store.append(str2[e:e+2])
    
    if not str1_store and not str2_store:
        return 65536

    c1 = str1_store.copy() 
    c2 = str1_store.copy()
    for i in str2_store:
        c2.append(i) if i not in c1 else c1.remove(i)
    
    intersec= []
    for i in str2_store:
        if i in str1_store: 
            str1_store.remove(i) 
            intersec.append(i)

    answer = len(intersec) / len(c2)
    return int(answer * 65536)