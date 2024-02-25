import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    else:
        div = []
        for k in range(1, n//2+1):
            if n % k == 0:
                div.append(k)
        if sum(div) == n:
            print(n, "=", end=" ")
            print(*div, sep=" + ")
        else:
            print(n, "is NOT perfect.")