from itertools import permutations
import math

def pn(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    store = []
    List = list(numbers)
    for i in range(1,len(List)+1):
        list_tmp = list(permutations(List, i))
        for j in set(list_tmp):
            element = "".join(list(j))
            if int(element) > 1 and pn(int(element)) == True and int(element) not in store:
                answer+=1
                store.append(int(element))
    return answer