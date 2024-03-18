from fractions import Fraction as f
def judge(a,b):
    while b!=1:
        if b%2==0:
            b=b//2
        elif b%5==0:
            b=b//5
        else:
            return 2
    return 1
def solution(a, b):
    k = f(a,b)
    return judge(k.numerator,k.denominator)