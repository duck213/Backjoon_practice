def solution(strs, t):
    INF = float('inf')
    n = len(t)
    dp = [INF]*(n+1)
    dp[0]=0
    word_set = set(strs)
    m_len = max(len(word) for word in strs)
    for s in range(1,n+1):
        for length in range(1, m_len+1):
            shard = t[s-length:s]
            if shard in word_set:
                dp[s] = min(dp[s], dp[s-length]+1)
                       
    return dp[n] if dp[n] < INF else -1