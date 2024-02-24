import sys
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for i in range(n)]
if sum(data) >= n//2+1:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")