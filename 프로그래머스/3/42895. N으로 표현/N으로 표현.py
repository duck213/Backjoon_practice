def solution(N, number):
    answer = 0
    dp = [[]]+ [[int(str(N) * i)] for i in range(1,9)]
    if N==number: return 1
    for i in range(2,9):
        for j in range(1,i):
            for k in dp[j]:
                for l in dp[i-j]:
                    dp[i].append(k+l)
                    dp[i].append(k-l)
                    dp[i].append(k*l)
                    if l!=0: dp[i].append(k//l)
        dp[i] = list(set(dp[i]))
        if number in dp[i]:
            return i

    return -1