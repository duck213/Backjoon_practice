from collections import defaultdict as de
def solution(array):
    answer = 0
    arr = de(int)
    cnt = []
    for i in array:
        arr[i]+= 1
    m = max(arr.values())
    for k,v in arr.items():
        if v==m:
            cnt.append(k)

    return cnt[0] if len(cnt)==1 else -1

