from collections import deque

def bfs(begin, target, words):
    cnt = 0
    start = begin
    length = len(target)
    while words:
        fin = 0
        out = False
        len_store = len(words)
        num_store = [0]*len_store
        for z,item in enumerate(words):
            fin = 0
            for i in range(length):
                if item[i]==start[i]:
                    num_store[z]+=1
                if start[i]==target[i]:
                    fin+=1

        if fin == length - 1:
            cnt += 1
            return cnt

        for item,s in zip(words,num_store):
            if s == length-1:
                start = item
                words.remove(item)
                cnt += 1
                out = True
                break
        if out: continue
        else:
            start = words.popleft()

    return cnt


def solution(begin, target, words):
    answer = 0
    words = deque(words)
    if target not in words:
        return answer
    else:
        answer = bfs(begin, target, words)
    return answer