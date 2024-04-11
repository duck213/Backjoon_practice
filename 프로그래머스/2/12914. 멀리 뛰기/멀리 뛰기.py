def solution(n):
    if n<=3: return n
    dp = [1,2,3] + [0]*1997
    for i in range(3,n):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n-1]%1234567