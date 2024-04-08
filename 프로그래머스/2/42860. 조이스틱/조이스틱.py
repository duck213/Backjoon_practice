from collections import defaultdict
def solution(name):
    if set(name) == {'A'}:
        return 0
    answer = 10000000
    length = len(name)
    dic = defaultdict(int)
    for item in range(65, 91):
        if item < 78:
            dic[chr(item)] = item - 65
        elif item >= 78:
            dic[chr(item)] = abs(item - 91)

    for i in range(length//2+1):
        right_sec = name[-i:] + name[:-i]
        left_sec = name[i::-1] + name[i+1:][::-1]
        for n in [right_sec,left_sec]:
            mini = []
            while n[-1]=='A':
                n = n[:-1]
            for e in n:
                mini.append(dic[str(e)])
            answer = min(sum(mini)+i+len(mini)-1, answer)
    return answer