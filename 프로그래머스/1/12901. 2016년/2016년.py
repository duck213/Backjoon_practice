from collections import deque
def solution(a, b):
    cal = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    filtered = deque(cal)
    if a in [1,4,7]:
        filtered.rotate(2)
    elif a in [2,8]:
        filtered.rotate(-1)
    elif a in [3,11]:
        filtered.rotate(-2)
    elif a in [6]:
        filtered.rotate(-3)
    elif a in [9,12]:
        filtered.rotate(+3)
    elif a in [10]:
        filtered.rotate(1)
    return filtered[b % 7 - 1]