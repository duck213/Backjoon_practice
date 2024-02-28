def solution(brown, yellow):
    divisors = []
    n = brown + yellow
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            divisors.append(i) 
            if (i**2)!=n : 
                divisors.append(n//i)
        if (i-2)*(n//i-2) == yellow:
            return [n//i,i]


    