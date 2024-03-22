def solution(m, n, puddles):
    store = [[0]*(m+1) for i in range(n+1)]
    store[0][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] not in puddles:
                store[i][j]=store[i-1][j]+store[i][j-1]
    return store[n][m]  % 1000000007