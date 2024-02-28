import re
def solution(s):
    temp = list(map(int, re.split("[ ]",s)))
    return str(min(temp))+" "+ str(max(temp))