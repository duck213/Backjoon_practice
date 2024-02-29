from itertools import product as pb
def solution(word):
    List = []
    for i in range(1,6):
        for item in list(pb(["A","E","I","O","U"], repeat=i)):
            pista = "".join(item)
            List.append(pista)
    List.sort()
    return List.index(word)+1