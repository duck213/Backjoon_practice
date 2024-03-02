def solution(price, money, count):
    num = 0
    for i in range(1,count+1):
        num += i*price
    return num - money if num > money else 0