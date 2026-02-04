
from fractions import gcd

def solution(arr):
    while len(arr) > 1: 
        a,b = arr.pop(),arr.pop()
        arr.append(a*b // gcd(a,b))

    return arr.pop()